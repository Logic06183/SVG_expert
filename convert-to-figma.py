#!/usr/bin/env python3
"""
Convert SVG slides from CSS classes to inline styles for Figma compatibility.
"""

import re
import sys
from pathlib import Path

def extract_css_classes(svg_content):
    """Extract CSS class definitions from SVG."""
    classes = {}
    style_block = re.search(r'<style>(.*?)</style>', svg_content, re.DOTALL)

    if not style_block:
        return classes

    style_content = style_block.group(1)

    # Extract each class definition
    class_pattern = r'\.(\w+(?:-\w+)*)\s*\{([^}]+)\}'
    for match in re.finditer(class_pattern, style_content):
        class_name = match.group(1)
        properties = match.group(2)

        # Parse properties
        props = {}
        for prop_match in re.finditer(r'([\w-]+):\s*([^;]+);', properties):
            prop_name = prop_match.group(1).strip()
            prop_value = prop_match.group(2).strip()

            # Convert CSS property names to SVG attribute names
            if prop_name == 'font-family':
                props['font-family'] = prop_value.replace("'Inter', sans-serif", "Inter, Arial, sans-serif").replace("'", "")
            elif prop_name == 'font-size':
                # Remove 'px' suffix
                props['font-size'] = prop_value.replace('px', '')
            elif prop_name == 'font-weight':
                props['font-weight'] = prop_value
            elif prop_name == 'fill':
                props['fill'] = prop_value
            elif prop_name == 'letter-spacing':
                # Convert letter-spacing from em to pixels (approximate)
                if 'em' in prop_value:
                    em_value = float(prop_value.replace('em', ''))
                    # Will be calculated per-text based on font-size
                    props['letter-spacing-em'] = em_value
            elif prop_name == 'font-style':
                props['font-style'] = prop_value

        classes[class_name] = props

    return classes

def convert_text_element(text_elem, classes):
    """Convert a text element from class to inline styles."""

    # Extract class name if present
    class_match = re.search(r'class="([\w-]+)"', text_elem)
    if not class_match:
        return text_elem

    class_name = class_match.group(1)
    if class_name not in classes:
        return text_elem

    props = classes[class_name]

    # Build inline style attributes
    inline_attrs = []

    if 'font-family' in props:
        inline_attrs.append(f'font-family="{props["font-family"]}"')
    if 'font-size' in props:
        font_size = props['font-size']
        inline_attrs.append(f'font-size="{font_size}"')

        # Calculate letter-spacing in pixels if specified
        if 'letter-spacing-em' in props:
            letter_spacing_px = float(font_size) * props['letter-spacing-em']
            inline_attrs.append(f'letter-spacing="{letter_spacing_px:.2f}"')
    if 'font-weight' in props:
        inline_attrs.append(f'font-weight="{props["font-weight"]}"')
    if 'fill' in props:
        inline_attrs.append(f'fill="{props["fill"]}"')
    if 'font-style' in props:
        inline_attrs.append(f'font-style="{props["font-style"]}"')

    # Remove class attribute
    result = re.sub(r'\s*class="[\w-]+"', '', text_elem)

    # Remove existing attributes that we're about to set (to avoid duplicates)
    result = re.sub(r'\s+font-family="[^"]*"', '', result)
    result = re.sub(r'\s+font-size="[^"]*"', '', result)
    result = re.sub(r'\s+font-weight="[^"]*"', '', result)
    result = re.sub(r'\s+fill="[^"]*"', '', result)
    result = re.sub(r'\s+letter-spacing="[^"]*"', '', result)
    result = re.sub(r'\s+font-style="[^"]*"', '', result)

    # Insert inline attributes before the closing >
    # Find the position before the first > (end of opening tag)
    close_pos = result.find('>')
    if close_pos != -1:
        # Insert inline attributes
        result = result[:close_pos] + ' ' + ' '.join(inline_attrs) + result[close_pos:]

    return result

def convert_svg_to_inline(svg_content):
    """Convert entire SVG from CSS classes to inline styles."""

    # Extract classes
    classes = extract_css_classes(svg_content)

    if not classes:
        print("No CSS classes found")
        return svg_content

    print(f"Found {len(classes)} CSS classes")

    # Remove @import line
    svg_content = re.sub(r"@import url\([^)]+\);?\s*", "", svg_content)

    # Convert all text elements
    text_pattern = r'<text[^>]*>(?:(?!</text>).)*</text>'

    def replace_text(match):
        return convert_text_element(match.group(0), classes)

    svg_content = re.sub(text_pattern, replace_text, svg_content, flags=re.DOTALL)

    # Remove the entire <style> block if it only contained class definitions
    svg_content = re.sub(r'<style>.*?</style>\s*', '', svg_content, flags=re.DOTALL)

    return svg_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert-to-figma.py <svg_file> [output_file]")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else input_file

    if not input_file.exists():
        print(f"Error: File {input_file} not found")
        sys.exit(1)

    print(f"Converting {input_file}...")

    svg_content = input_file.read_text(encoding='utf-8')
    converted = convert_svg_to_inline(svg_content)

    output_file.write_text(converted, encoding='utf-8')
    print(f"✓ Converted and saved to {output_file}")

if __name__ == '__main__':
    main()
