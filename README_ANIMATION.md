# Animation Export Worktree

This git worktree is dedicated to converting SVG animations to MP4 and GIF formats for PowerPoint presentations.

## Setup

### 1. Install System Dependencies

```bash
# Install ffmpeg (required for MP4 conversion)
brew install ffmpeg

# Install chromedriver (required for rendering)
brew install chromedriver

# Optional: Install gifsicle (for GIF optimization)
brew install gifsicle
```

### 2. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Make the Scripts Executable

```bash
chmod +x convert_animations.py
chmod +x convert_all.sh
```

## Usage

### Convert Single Animation

```bash
./convert_animations.py visualization_scripts/outputs/animations/gradient_descent_animation.svg
```

### Convert Multiple Animations

```bash
./convert_animations.py \
    visualization_scripts/outputs/animations/gradient_descent_animation.svg \
    visualization_scripts/outputs/animations/decision_tree_building.svg
```

### Convert All Animations

```bash
./convert_all.sh
```

### Specify Output Format

```bash
# MP4 only
./convert_animations.py -f mp4 animation.svg

# GIF only
./convert_animations.py -f gif animation.svg

# Both (default)
./convert_animations.py -f mp4 gif animation.svg
```

### Custom Settings

```bash
./convert_animations.py \
    --fps 60 \
    --duration 15 \
    --output my_exports \
    animation.svg
```

## Options

- `-o, --output DIR`: Output directory (default: `converted_animations`)
- `-f, --format`: Output format(s): `mp4`, `gif` (default: both)
- `--fps N`: Frames per second (default: 30)
- `--duration N`: Duration in seconds (default: 10)
- `--keep-frames`: Keep temporary frame files

## Output

Converted files will be saved in the `converted_animations` directory:

```
converted_animations/
├── gradient_descent_animation.mp4
├── gradient_descent_animation.gif
├── decision_tree_building.mp4
├── decision_tree_building.gif
└── ...
```

## PowerPoint Usage

### Inserting MP4 Videos

1. In PowerPoint, go to **Insert** → **Video** → **Video from File**
2. Select your `.mp4` file
3. The video will play automatically or on click (configurable)

### Inserting GIF Animations

1. In PowerPoint, go to **Insert** → **Pictures** → **Picture from File**
2. Select your `.gif` file
3. The GIF will loop automatically in presentation mode

## Tips

- **MP4 files** are generally smaller and have better quality
- **GIF files** are easier to insert and work on all platforms
- For best quality, use `--fps 60` for smoother animations
- Adjust `--duration` to match your animation's actual length
- Use `--keep-frames` if you want to edit individual frames

## Troubleshooting

### "chromedriver not found"

```bash
brew install chromedriver
# If you get security warnings on macOS:
xattr -d com.apple.quarantine $(which chromedriver)
```

### "ffmpeg not found"

```bash
brew install ffmpeg
```

### Low quality output

Increase FPS and ensure your source SVG has good resolution:

```bash
./convert_animations.py --fps 60 animation.svg
```

### Animation too short/long

Adjust the duration parameter:

```bash
./convert_animations.py --duration 15 animation.svg
```

## Going Back to Main Worktree

```bash
cd ../SVG_expert
```

## Removing This Worktree

When you're done:

```bash
cd ../SVG_expert
git worktree remove ../SVG_expert_animation_export
```
