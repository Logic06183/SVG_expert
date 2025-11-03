#!/bin/bash

# Convert all SVG animations in the animations directory to MP4 and GIF

ANIMATIONS_DIR="visualization_scripts/outputs/animations"
OUTPUT_DIR="converted_animations"

echo "=================================================="
echo "Converting All SVG Animations"
echo "=================================================="
echo ""
echo "Source: $ANIMATIONS_DIR"
echo "Output: $OUTPUT_DIR"
echo ""

# Find all SVG files in the animations directory
SVG_FILES=$(find "$ANIMATIONS_DIR" -name "*.svg" -type f | grep -E "(gradient_descent|decision_tree|random_forest|backpropagation|learning_rate|feature_importance|bias_variance|gradient_boosting|hyperparameter|double_descent)")

if [ -z "$SVG_FILES" ]; then
    echo "No animation SVG files found in $ANIMATIONS_DIR"
    exit 1
fi

echo "Found animations to convert:"
echo "$SVG_FILES" | while read file; do
    echo "  - $(basename "$file")"
done
echo ""

# Convert each file
echo "$SVG_FILES" | while read svg_file; do
    ./convert_animations.py \
        --output "$OUTPUT_DIR" \
        --format mp4 gif \
        --fps 30 \
        --duration 10 \
        "$svg_file"
done

echo ""
echo "=================================================="
echo "Conversion Complete!"
echo "=================================================="
echo ""
echo "Your converted files are in: $OUTPUT_DIR"
echo ""
echo "To use in PowerPoint:"
echo "  - MP4: Insert → Video → Video from File"
echo "  - GIF: Insert → Pictures → Picture from File"
echo ""
