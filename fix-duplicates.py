#!/usr/bin/env python3
"""
Fix duplicate attributes in SVG files caused by the buggy conversion script.
"""

import re
import sys
from pathlib import Path

def remove_duplicate_attributes(text_elem):
    """Remove duplicate attributes from a text element, keeping the last occurrence."""

    # Extract the opening tag
    tag_match = re.match(r'(<text[^>]*>)', text_elem)
    if not tag_match:
        return text_elem

    opening_tag = tag_match.group(1)
    rest = text_elem[len(opening_tag):]

    # Extract all attributes
    attr_pattern = r'(\w+(?:-\w+)*)="([^"]*)"'
    attributes = {}
    attr_order = []

    for match in re.finditer(attr_pattern, opening_tag):
        attr_name = match.group(1)
        attr_value = match.group(2)

        # If attribute already exists, we're keeping the last one
        if attr_name not in attributes:
            attr_order.append(attr_name)

        attributes[attr_name] = attr_value

    # Rebuild the opening tag with unique attributes
    new_tag = '<text'
    for attr_name in attr_order:
        new_tag += f' {attr_name}="{attributes[attr_name]}"'
    new_tag += '>'

    return new_tag + rest

def fix_svg_duplicates(svg_content):
    """Fix all duplicate attributes in SVG text elements."""

    # Match all text elements
    text_pattern = r'<text[^>]*>(?:(?!</text>).)*</text>'

    def replace_text(match):
        return remove_duplicate_attributes(match.group(0))

    return re.sub(text_pattern, replace_text, svg_content, flags=re.DOTALL)

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix-duplicates.py <svg_file> [output_file]")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else input_file

    if not input_file.exists():
        print(f"Error: File {input_file} not found")
        sys.exit(1)

    print(f"Fixing duplicates in {input_file}...")

    svg_content = input_file.read_text(encoding='utf-8')
    fixed = fix_svg_duplicates(svg_content)

    output_file.write_text(fixed, encoding='utf-8')
    print(f"✓ Fixed and saved to {output_file}")

if __name__ == '__main__':
    main()
