#!/usr/bin/env python3
"""
Animation to MP4/GIF Converter
Converts SVG animations to MP4 videos and GIF files for PowerPoint presentations

Requirements:
- selenium
- pillow
- ffmpeg (installed via homebrew)
"""

import os
import sys
import time
import argparse
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import subprocess

class AnimationConverter:
    def __init__(self, output_dir="converted_animations", fps=30, duration=10):
        self.output_dir = Path(output_dir).resolve()
        self.output_dir.mkdir(exist_ok=True)
        self.fps = fps
        self.duration = duration
        self.frames_dir = self.output_dir / "frames"
        self.frames_dir.mkdir(exist_ok=True)

    def setup_browser(self):
        """Setup headless Chrome browser"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        try:
            # Use webdriver-manager to automatically download the correct chromedriver version
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e:
            print(f"Error setting up Chrome driver: {e}")
            print("Make sure Chrome browser is installed")
            sys.exit(1)

    def capture_frames(self, svg_file, animation_name):
        """Capture frames from animated SVG"""
        print(f"Capturing frames for {animation_name}...")

        # Read SVG content
        svg_path = Path(svg_file).resolve()
        with open(svg_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()

        # Create HTML wrapper with embedded SVG
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    background: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    width: 100vw;
                    overflow: hidden;
                }}
                #container {{
                    width: 100%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                svg {{
                    max-width: 100vw;
                    max-height: 100vh;
                    width: auto;
                    height: auto;
                }}
            </style>
        </head>
        <body>
            <div id="container">
                {svg_content}
            </div>
            <script>
                // Force animations to start
                document.querySelectorAll('animate, animateTransform').forEach(el => {{
                    el.beginElement();
                }});
            </script>
        </body>
        </html>
        """

        # Save temporary HTML file
        temp_html = self.output_dir / "temp_viewer.html"
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Load in browser
        self.driver.get(temp_html.as_uri())
        time.sleep(3)  # Wait for SVG to load and animations to start

        # Capture frames
        frame_files = []
        total_frames = self.fps * self.duration

        for i in range(total_frames):
            frame_path = self.frames_dir / f"{animation_name}_frame_{i:04d}.png"
            self.driver.save_screenshot(str(frame_path))
            frame_files.append(frame_path)

            # Small delay between frames
            time.sleep(1 / self.fps)

            if (i + 1) % 30 == 0:
                print(f"  Captured {i + 1}/{total_frames} frames...")

        print(f"  Captured all {total_frames} frames")
        return frame_files

    def frames_to_mp4(self, animation_name):
        """Convert captured frames to MP4 video"""
        print(f"Creating MP4 for {animation_name}...")

        input_pattern = str(self.frames_dir / f"{animation_name}_frame_%04d.png")
        output_file = self.output_dir / f"{animation_name}.mp4"

        cmd = [
            'ffmpeg',
            '-y',  # Overwrite output file
            '-framerate', str(self.fps),
            '-i', input_pattern,
            '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2',  # Ensure dimensions are divisible by 2
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-crf', '23',  # Quality (lower = better, 23 is good default)
            str(output_file)
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"  Created: {output_file}")
            return output_file
        except subprocess.CalledProcessError as e:
            print(f"  Error creating MP4: {e.stderr.decode()}")
            return None

    def frames_to_gif(self, animation_name, optimize=True):
        """Convert captured frames to GIF"""
        print(f"Creating GIF for {animation_name}...")

        frame_files = sorted(self.frames_dir.glob(f"{animation_name}_frame_*.png"))

        if not frame_files:
            print(f"  No frames found for {animation_name}")
            return None

        # Load all frames
        frames = []
        for frame_file in frame_files:
            img = Image.open(frame_file)
            frames.append(img)

        output_file = self.output_dir / f"{animation_name}.gif"

        # Save as GIF
        frames[0].save(
            output_file,
            save_all=True,
            append_images=frames[1:],
            duration=int(1000 / self.fps),  # Duration per frame in ms
            loop=0,  # Infinite loop
            optimize=optimize
        )

        print(f"  Created: {output_file}")

        # Optionally optimize with gifsicle if available
        if optimize:
            try:
                subprocess.run([
                    'gifsicle',
                    '-O3',
                    '--colors', '256',
                    str(output_file),
                    '-o', str(output_file)
                ], check=True, capture_output=True)
                print(f"  Optimized GIF with gifsicle")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"  (gifsicle not found, skipping optimization)")

        return output_file

    def cleanup_frames(self, animation_name):
        """Remove temporary frame files"""
        frame_files = self.frames_dir.glob(f"{animation_name}_frame_*.png")
        for frame_file in frame_files:
            frame_file.unlink()

    def convert(self, svg_file, output_formats=['mp4', 'gif'], cleanup=True):
        """Convert SVG animation to specified formats"""
        animation_name = Path(svg_file).stem

        print(f"\n{'='*60}")
        print(f"Converting: {animation_name}")
        print(f"{'='*60}")

        # Capture frames
        self.capture_frames(svg_file, animation_name)

        # Convert to requested formats
        outputs = {}

        if 'mp4' in output_formats:
            mp4_file = self.frames_to_mp4(animation_name)
            if mp4_file:
                outputs['mp4'] = mp4_file

        if 'gif' in output_formats:
            gif_file = self.frames_to_gif(animation_name)
            if gif_file:
                outputs['gif'] = gif_file

        # Cleanup
        if cleanup:
            print(f"Cleaning up temporary frames...")
            self.cleanup_frames(animation_name)

        return outputs

    def close(self):
        """Close the browser"""
        if hasattr(self, 'driver'):
            self.driver.quit()


def main():
    parser = argparse.ArgumentParser(
        description='Convert SVG animations to MP4 and GIF for PowerPoint'
    )
    parser.add_argument(
        'input',
        nargs='+',
        help='SVG file(s) to convert'
    )
    parser.add_argument(
        '-o', '--output',
        default='converted_animations',
        help='Output directory (default: converted_animations)'
    )
    parser.add_argument(
        '-f', '--format',
        nargs='+',
        choices=['mp4', 'gif'],
        default=['mp4', 'gif'],
        help='Output format(s) (default: mp4 gif)'
    )
    parser.add_argument(
        '--fps',
        type=int,
        default=30,
        help='Frames per second (default: 30)'
    )
    parser.add_argument(
        '--duration',
        type=int,
        default=10,
        help='Duration in seconds (default: 10)'
    )
    parser.add_argument(
        '--keep-frames',
        action='store_true',
        help='Keep temporary frame files'
    )

    args = parser.parse_args()

    # Create converter
    converter = AnimationConverter(
        output_dir=args.output,
        fps=args.fps,
        duration=args.duration
    )

    try:
        converter.setup_browser()

        # Convert each input file
        for svg_file in args.input:
            if not os.path.exists(svg_file):
                print(f"Warning: File not found: {svg_file}")
                continue

            converter.convert(
                svg_file,
                output_formats=args.format,
                cleanup=not args.keep_frames
            )

        print(f"\n{'='*60}")
        print(f"All conversions complete!")
        print(f"Output directory: {converter.output_dir.resolve()}")
        print(f"{'='*60}")

    finally:
        converter.close()


if __name__ == '__main__':
    main()
