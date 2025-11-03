# 3Blue1Brown Style ML Animations

Professional-quality machine learning animations created in the distinctive visual style of Grant Sanderson's 3Blue1Brown educational videos.

## Files in this Directory

### Animations (SVG with SMIL)

1. **gradient_descent_3b1b_style.svg** (13 KB)
   - Dual comparison: Local minimum (red) vs Global minimum (blue)
   - 3D contour plots with gradient vectors
   - Animated descent paths with motion trails
   - Formula overlay with learning rate explanation
   - Duration: ~25 seconds, loops seamlessly

2. **neural_network_3b1b_style.svg** (20 KB)
   - 3-layer network (4→6→3) with glowing nodes
   - Forward pass (blue wave) and backward pass (red wave)
   - Real-time loss curve visualization
   - Split screen: Network + Training graph
   - Duration: ~30 seconds

3. **decision_tree_3b1b_style.svg** (18 KB)
   - Scatter plot with climate-health data
   - Animated split line with Gini impurity calculation
   - Dual view: Data visualization + Tree structure
   - Region shading by purity (gradient from mixed to pure)
   - Duration: ~25 seconds

4. **gradient_boosting_3b1b_style.svg** (20 KB)
   - Three-panel dashboard layout
   - Top: Predictions vs True values (improving over time)
   - Middle: Residual bars shrinking
   - Bottom: Current weak learner tree
   - Formula: F_m = F_{m-1} + η·h_m
   - Duration: ~30 seconds

5. **double_descent_3b1b_style.svg** (16 KB)
   - Professional plot with three regime backgrounds
   - Classical U-curve (dotted) vs Modern behavior (solid)
   - Interpolation threshold marked
   - Inset plots showing model fit at key points
   - "Surprise!" emphasis at second descent
   - Duration: ~25 seconds

### Documentation

6. **3B1B_STYLE_GUIDE.md** (18 KB)
   - Comprehensive style guide explaining all design decisions
   - Color palette reference (exact hex codes)
   - Typography hierarchy and font specifications
   - Animation timing and easing guidelines
   - Layout system and spacing rules
   - Customization instructions
   - Comparison with previous versions

## Quick Start

### Viewing Animations

**In Browser:**
```bash
# Open any SVG file directly in a modern browser
open gradient_descent_3b1b_style.svg
```

**In Figma:**
1. Drag SVG file into Figma canvas
2. Ungroup to access layers
3. Edit with full fidelity
4. Animations preserved in SVG code

**In Adobe Illustrator:**
1. File → Open → Select SVG
2. Layers panel shows structure
3. Edit visuals
4. Save as SVG (preserve animations)

### Customization

**Quick color change:**
```svg
<!-- Find in SVG file -->
<stop offset="0%" style="stop-color:#29ABCA"/>
<!-- Replace with your color -->
<stop offset="0%" style="stop-color:#YOUR_HEX"/>
```

**Adjust animation speed:**
```svg
<!-- Find animation tags -->
<animate dur="2s"/>
<!-- Change duration -->
<animate dur="1s"/>
```

See **3B1B_STYLE_GUIDE.md** for detailed customization instructions.

## Key Features

### Visual Style
- **Dark theme:** #111111 background (3B1B standard)
- **Color palette:** Blue (#29ABCA) positive, Red (#FC6255) negative
- **Typography:** SF Pro Display for UI, SF Mono for code
- **Glowing effects:** Gaussian blur filters for emphasis
- **Smooth gradients:** HSL interpolation for natural transitions

### Animation Techniques
- **LaggedStart:** Staggered reveals (lag_ratio 0.1-0.5)
- **ShowCreation:** Stroke-dasharray path drawing
- **Motion paths:** Smooth bezier curve movements
- **Easing:** Cubic bezier timing functions
- **Glow pulses:** Ambient animations on key elements

### Professional Polish
- **1920×1080 resolution** (Full HD)
- **Generous margins** (50-100px from edges)
- **Visual hierarchy** (title → content → formulas)
- **Semantic colors** (meaning beyond aesthetics)
- **Proper math notation** (LaTeX-style rendering)
- **Accessibility** (high contrast, colorblind-safe)

## Technical Specifications

### SVG Structure
```
Background layer (rect #111111)
├─ Title group (fade in)
├─ Main content groups
│  ├─ Left panel / Plot
│  ├─ Right panel / Graph
│  └─ Overlays
├─ Formula layer (bottom)
└─ Metadata (watermark)
```

### Color Codes Reference

**Primary Palette:**
```
Background:    #111111
Text:          #FFFFFF, #EEEEEE
Blue (data):   #29ABCA
Red (error):   #FC6255
Green (good):  #27AE60
Yellow (key):  #FFFF00
Gray (axes):   #444444, #666666, #888888
```

**Gradients:**
- Blue gradient: #1C758A → #29ABCA
- Red gradient: #CF5044 → #FC6255
- Error scale: #FC6255 (high) → #E0A856 (mid) → #27AE60 (low)

### Animation Timing

**Standard durations:**
- Quick: 0.3-0.5s (state changes)
- Normal: 0.8-1.5s (reveals)
- Slow: 2-3s (complex paths)
- Ambient: 3-5s (loops)

**Lag ratios:**
- Tight: 0.05-0.1
- Standard: 0.1-0.3
- Dramatic: 0.5-0.8

## Design Principles

From analysis of 3Blue1Brown's official manim repository:

1. **Color conveys information** - Blue=correct, Red=error, Yellow=important
2. **Animation guides attention** - Progressive disclosure, not simultaneous
3. **White space is valuable** - Generous margins, deliberate spacing
4. **Typography creates hierarchy** - Size, weight, color for importance
5. **Consistency builds trust** - Same patterns throughout
6. **Math should be beautiful** - Proper LaTeX rendering, thoughtful layout

## Differences from Standard Visualizations

### Before (Standard)
- Light backgrounds
- Generic rainbow colors
- All elements appear at once
- Single font
- No emphasis effects
- Cramped layouts

### After (3B1B Style)
- Dark background (#111111)
- Semantic color palette (blue/red/green)
- LaggedStart sequential reveals
- Font hierarchy (display/mono)
- Gaussian blur glows on key elements
- Generous margins and white space

**Result:** Professional, engaging, educational quality matching YouTube's top science communicators.

## Use Cases

### Education
- Online courses (embed in slides)
- YouTube videos (export to video)
- Interactive notebooks (Jupyter, Observable)
- Blog posts (inline SVG)

### Presentations
- Conference talks (PowerPoint, Keynote)
- Research presentations (Beamer, reveal.js)
- Product demos (Figma prototypes)

### Documentation
- Technical documentation
- API guides
- Research papers (as figures)
- Blog posts and articles

### Social Media
- Twitter/X cards (resize to 1200×675)
- LinkedIn posts (1200×1200)
- Instagram stories (1080×1920)

## Export Formats

### Video (for PowerPoint/Keynote)
```bash
# Using ffmpeg
ffmpeg -i gradient_descent_3b1b_style.svg -t 25 -pix_fmt yuv420p output.mp4
```

### Static PNG (for papers)
```bash
# Using Inkscape
inkscape gradient_descent_3b1b_style.svg --export-png=output.png --export-dpi=300
```

### Optimized SVG (for web)
```bash
# Using svgo
svgo gradient_descent_3b1b_style.svg -o output_optimized.svg
```

## Credits

**Created by:** Claude Code (Anthropic)
**Inspired by:** 3Blue1Brown (Grant Sanderson)
**Style source:** github.com/3b1b/manim
**Date:** November 2025

**Recommended citation:**
```
"ML visualizations styled after 3Blue1Brown's educational animations"
```

## License

These visualizations are provided for educational purposes. The 3Blue1Brown visual style is strongly associated with Grant Sanderson's work - please credit appropriately when using similar styling.

## Additional Resources

- **3Blue1Brown YouTube:** youtube.com/@3blue1brown
- **Manim Repository:** github.com/3b1b/manim
- **Community Manim:** github.com/ManimCommunity/manim
- **Style Guide:** See 3B1B_STYLE_GUIDE.md in this directory

## Support

For questions about:
- **Customization:** See 3B1B_STYLE_GUIDE.md § Customization Guide
- **Technical issues:** Check SVG structure and filter compatibility
- **Design decisions:** See 3B1B_STYLE_GUIDE.md § Manim Insights

---

*Last updated: November 3, 2025*
