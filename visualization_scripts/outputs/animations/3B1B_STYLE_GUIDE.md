# 3Blue1Brown Style Guide for ML Animations

This document explains the styling techniques, color palettes, and animation principles used in our enhanced ML visualizations, based on analysis of Grant Sanderson's official 3Blue1Brown manim repository.

## Table of Contents
1. [Color Palette](#color-palette)
2. [Typography](#typography)
3. [Animation Techniques](#animation-techniques)
4. [Layout & Spacing](#layout--spacing)
5. [Visual Components](#visual-components)
6. [Mathematical Notation](#mathematical-notation)
7. [Differences from Previous Versions](#differences-from-previous-versions)
8. [Customization Guide](#customization-guide)

---

## Color Palette

### Primary Colors (3B1B Standard)

Based on analysis of the official manim repository, Grant Sanderson uses a carefully curated color palette:

#### Background & Text
```
Background:       #111111  (very dark gray, not pure black)
Text Primary:     #FFFFFF  (white)
Text Secondary:   #EEEEEE  (light gray)
Text Tertiary:    #888888  (medium gray)
Grid/Axes:        #444444  (dark gray, subtle)
Panel Background: #1A1A1A  (slightly lighter than main bg)
```

#### Data Visualization Colors

**Positive Values (Blue Gradient):**
```
BLUE_E:  #1C758A  (darker blue)
BLUE_D:  #2485A8  (medium-dark blue)
BLUE_C:  #29ABCA  (standard blue) ← Primary blue
BLUE_B:  #58C4DD  (light blue)
BLUE_A:  #9CDCEB  (very light blue)
```

**Negative Values (Red Gradient):**
```
RED_E:   #CF5044  (darker red)
RED_D:   #E07856  (orange-red)
RED_C:   #FC6255  (standard red) ← Primary red
RED_B:   #FF8080  (light red)
RED_A:   #F7A1A3  (very light red)
```

**Additional Semantic Colors:**
```
Success:   #27AE60  (green)
Warning:   #FF6B35  (orange)
Emphasis:  #FFFF00  (yellow)
Neutral:   #666666  (gray)
```

### Color Usage Guidelines

1. **Use blue (#29ABCA) for:**
   - Correct predictions
   - Successful optimization paths
   - Primary data series
   - Neural network forward pass
   - Low error states

2. **Use red (#FC6255) for:**
   - Errors/residuals
   - Failed optimization paths
   - High loss values
   - Backward pass gradients
   - Warning states

3. **Use green (#27AE60) for:**
   - Improvements
   - Success indicators
   - Final optimal states
   - Achievement markers

4. **Use yellow (#FFFF00) for:**
   - Emphasis on key formulas
   - Learning rate parameters
   - Important thresholds
   - Surprise/attention markers

### HSL Color Interpolation

For smooth gradients (especially in neural networks), 3B1B uses HSL interpolation rather than RGB:

```python
# Example from manim codebase
def interpolate_color(color1, color2, alpha):
    # Convert to HSL, interpolate, convert back
    # This produces smoother, more natural color transitions
```

Applied in our animations:
- Neural network activation values
- Loss surface gradients
- Error magnitude visualization

---

## Typography

### Font Families

**Primary Font (UI Text):**
```css
font-family: 'SF Pro Display', 'Lato', 'Helvetica Neue', sans-serif;
```

**Code/Numbers Font:**
```css
font-family: 'SF Mono', 'Menlo', 'Monaco', monospace;
```

**Mathematical Font:**
- Use proper LaTeX rendering for formulas
- Greek letters: θ, α, η, ∇, Σ
- Proper subscripts/superscripts

### Font Sizes (at 1920×1080)

```
Titles:           64-72px  (bold)
Subtitles:        28-32px  (regular)
Panel Headers:    32-36px  (bold)
Body Text:        20-24px  (regular)
Labels:           18-22px  (regular)
Values/Numbers:   20-28px  (monospace)
Formulas:         36-48px  (LaTeX)
Small Labels:     16-18px  (regular)
Watermarks:       14-18px  (light)
```

### Text Styling Principles

1. **Hierarchy:** Size, weight, and color establish visual hierarchy
2. **Contrast:** Minimum 4.5:1 contrast ratio (white on #111111 = 18.6:1)
3. **Alignment:** Left for paragraphs, center for titles, end for numbers
4. **Spacing:** Generous line height (1.4-1.6)
5. **Emphasis:** Color > weight > size for importance

---

## Animation Techniques

### Core Animation Patterns (from manim)

#### 1. LaggedStart
Staggered reveals create visual flow:
```python
# Manim pattern
LaggedStartMap(FadeIn, objects, lag_ratio=0.1)
```

**SVG Implementation:**
```svg
<animate attributeName="opacity" from="0" to="1"
         begin="0s" dur="0.5s" fill="freeze"/>
<animate attributeName="opacity" from="0" to="1"
         begin="0.1s" dur="0.5s" fill="freeze"/>
<animate attributeName="opacity" from="0" to="1"
         begin="0.2s" dur="0.5s" fill="freeze"/>
```

**Applied in:**
- Data points appearing
- Neural network nodes activating
- Tree nodes building
- Formula components

#### 2. ShowCreation (Line Drawing)
Smooth path reveals:
```python
# Manim pattern
ShowCreation(curve, run_time=2, lag_ratio=0.01)
```

**SVG Implementation:**
```svg
<path stroke-dasharray="1000" stroke-dashoffset="1000">
  <animate attributeName="stroke-dashoffset"
           from="1000" to="0" dur="2s" fill="freeze"/>
</path>
```

**Applied in:**
- Loss curves drawing
- Decision tree splits
- Gradient descent paths
- Network connections

#### 3. FadeIn with Scale
Emphasis on appearance:
```python
# Manim pattern
FadeIn(object, scale=1.2)
```

**SVG Implementation:**
```svg
<g opacity="0" transform="scale(0.8)">
  <animate attributeName="opacity" from="0" to="1" dur="0.5s"/>
  <animateTransform attributeName="transform" type="scale"
                    from="0.8" to="1" dur="0.5s"/>
</g>
```

**Applied in:**
- Success/failure indicators
- Formula highlights
- Key results

#### 4. Motion Along Path
Smooth transitions:
```python
# Manim pattern
MoveAlongPath(ball, path, run_time=3)
```

**SVG Implementation:**
```svg
<animateMotion dur="3s" fill="freeze"
               path="M 100,100 Q 200,50 300,100"/>
```

**Applied in:**
- Gradient descent ball
- Forward/backward pass waves
- Progress indicators

### Timing Guidelines

**Based on 3B1B video analysis:**

```
Quick transitions:    0.3-0.5s  (state changes)
Standard animations:  0.8-1.5s  (main reveals)
Complex movements:    2-3s      (paths, transformations)
Dramatic emphasis:    1-2s      (key moments)
Ambient loops:        3-5s      (continuous effects)
```

**Lag Ratios:**
```
Tight sequence:   0.05-0.1  (rapid succession)
Standard flow:    0.1-0.3   (comfortable pace)
Dramatic pause:   0.5-0.8   (building anticipation)
```

### Easing Functions

3B1B uses sophisticated easing for natural motion:

```
smooth_in_out:     Start slow, accelerate, slow down
ease_out_cubic:    Quick start, gradual slow
ease_in_cubic:     Gradual start, quick end
linear:            Only for continuous loops
```

**Our SVG equivalents:**
- Use keyTimes and keySplines for bezier easing
- Apply to transforms, opacity, colors

---

## Layout & Spacing

### Screen Resolution
**Standard:** 1920×1080 (Full HD)
- 16:9 aspect ratio
- Designed for YouTube display
- Scales well to 4K

### Margin System
```
Edge margins:      50-100px   (keep content safe)
Panel padding:     20-30px    (internal spacing)
Element spacing:   15-25px    (between related items)
Group separation:  40-60px    (between sections)
```

### buff Parameter (from manim)
In manim, `buff` controls spacing. Our equivalents:

```
SMALL_BUFF:        10-15px
MED_SMALL_BUFF:    15-20px
MED_BUFF:          20-25px
LARGE_BUFF:        40-60px
```

### Grid System
Our animations use implicit grids:

**Three-column layout:** 640px each (gradient boosting)
**Two-column layout:** 960px each (decision tree)
**Single focus:** 1520px wide (double descent plot)

### Visual Hierarchy

1. **Title layer** (top 150px)
   - Main title
   - Subtitle/description

2. **Content layer** (middle 750px)
   - Primary visualizations
   - Interactive elements

3. **Formula/info layer** (bottom 180px)
   - Mathematical notation
   - Legends, metadata
   - Progress indicators

---

## Visual Components

### 1. Glowing Effects

**Node Glow (subtle):**
```svg
<filter id="nodeGlow">
  <feGaussianBlur stdDeviation="3"/>
  <feMerge>
    <feMergeNode in="coloredBlur"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

**Strong Glow (emphasis):**
```svg
<filter id="strongGlow">
  <feGaussianBlur stdDeviation="6"/>
  <feMerge>
    <feMergeNode in="coloredBlur"/>
    <feMergeNode in="coloredBlur"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

**Applied to:**
- Active neural network nodes
- Optimal points
- Success indicators
- Emphasis markers

### 2. Gradients

**Linear gradients for transitions:**
```svg
<linearGradient id="errorGradient">
  <stop offset="0%" stop-color="#FC6255"/>   <!-- High error -->
  <stop offset="50%" stop-color="#E0A856"/>  <!-- Medium -->
  <stop offset="100%" stop-color="#27AE60"/> <!-- Low error -->
</linearGradient>
```

**Radial gradients for glows:**
```svg
<radialGradient id="glowBlue">
  <stop offset="0%" stop-color="#29ABCA" stop-opacity="0.8"/>
  <stop offset="100%" stop-color="#29ABCA" stop-opacity="0"/>
</radialGradient>
```

### 3. Arrows and Markers

**3B1B style arrows:**
- Filled triangle heads
- Consistent with stroke color
- Smooth curves with path_arc

```svg
<marker id="arrowBlue" markerWidth="10" markerHeight="10"
        refX="9" refY="3" orient="auto">
  <path d="M0,0 L0,6 L9,3 z" fill="#29ABCA"/>
</marker>
```

### 4. Rounded Rectangles

All panels and containers use subtle rounding:
```svg
<rect rx="8" ry="8"/>  <!-- Standard rounding -->
<rect rx="12" ry="12"/> <!-- Emphasis panels -->
```

### 5. Stroke Weights

**Hierarchical strokes:**
```
Panel borders:     2-3px   (structure)
Axes:              2-3px   (reference)
Primary curves:    4-5px   (data)
Connections:       1-3px   (relationships, varies by weight)
Emphasis:          4-6px   (highlights)
Grid:              1px     (subtle background)
```

---

## Mathematical Notation

### LaTeX-Style Rendering

**3B1B uses proper mathematical typography:**

1. **Greek letters:** θ, α, η, ∇, Σ, β, λ
2. **Subscripts/superscripts:** Use baseline-shift in SVG
3. **Operators:** Proper spacing around =, +, −, ·
4. **Fractions:** Stacked with proper sizing
5. **Matrices:** Aligned bracketed notation

### Formula Styling

**Primary formulas (large display):**
```svg
<text font-size="48" fill="#EEEEEE">
  <tspan>θ</tspan>
  <tspan baseline-shift="sub" font-size="32">new</tspan>
  <tspan> = θ</tspan>
  <tspan baseline-shift="sub" font-size="32">old</tspan>
  <tspan> − </tspan>
  <tspan fill="#FFFF00">α</tspan>
  <tspan fill="#29ABCA">∇</tspan>
  <tspan>L(θ)</tspan>
</text>
```

**Inline formulas (integrated):**
```svg
<text font-size="24">
  Gini: <tspan font-family="monospace">G = 1 − Σp²</tspan>
</text>
```

### Color Coding in Formulas

- **Variables:** White/light gray (#EEEEEE)
- **Parameters (tunable):** Yellow (#FFFF00)
- **Operators (special):** Blue (#29ABCA)
- **Results:** Green (#27AE60) or context-specific

---

## Differences from Previous Versions

### What Changed

#### 1. Background
**Before:** Light backgrounds (#FFFFFF) or medium grays
**After:** Very dark gray (#111111) for 3B1B consistency
**Why:** Reduces eye strain, better contrast, professional appearance

#### 2. Color Palette
**Before:** Generic rainbow, arbitrary colors
**After:** Purposeful blue/red gradients with semantic meaning
**Why:** Color conveys information (blue=good, red=error)

#### 3. Animation Timing
**Before:** All elements appear simultaneously or with linear timing
**After:** LaggedStart reveals, smooth easing, progressive disclosure
**Why:** Guides viewer attention, creates narrative flow

#### 4. Typography
**Before:** Single font, inconsistent sizing
**After:** Font hierarchy (display/mono), proper LaTeX math
**Why:** Professional appearance, readability, mathematical correctness

#### 5. Glow Effects
**Before:** None or harsh drop shadows
**After:** Subtle Gaussian blur glows on important elements
**Why:** Draws attention without being distracting

#### 6. Layout Density
**Before:** Cramped, edge-to-edge content
**After:** Generous margins (50-100px), deliberate white space
**Why:** Easier to focus, professional composition

#### 7. Visual Hierarchy
**Before:** Flat design, everything same weight
**After:** Clear size/color/opacity hierarchy
**Why:** Viewer knows where to look first

### Technical Improvements

1. **SVG Structure:**
   - Named groups for Figma compatibility
   - Organized layers (background → content → overlays)
   - Semantic IDs (leftPanel, rightPanel, etc.)

2. **Animation Orchestration:**
   - Synchronized timing across elements
   - Progressive reveal (builds complexity)
   - Looping ambient effects

3. **Accessibility:**
   - High contrast ratios (18:1 for primary text)
   - Colorblind-safe palette
   - Clear visual encoding beyond color alone

---

## Customization Guide

### How to Adapt These Animations

#### 1. Changing Colors

**To match your brand:**
```svg
<!-- Replace primary blue -->
<stop stop-color="#29ABCA"/>  <!-- Original -->
<stop stop-color="#YOUR_COLOR"/>  <!-- Your brand -->
```

**Maintain contrast ratios:**
- Check with WebAIM contrast checker
- Aim for minimum 4.5:1 (text)
- Maintain semantic meaning (red=bad, green=good)

#### 2. Adjusting Timing

**Speed up animations:**
```svg
<!-- Original -->
<animate dur="2s"/>
<!-- Faster -->
<animate dur="1s"/>
```

**Change lag ratio:**
```svg
<!-- Original (0.1s lag) -->
begin="0s", begin="0.1s", begin="0.2s"
<!-- Faster (0.05s lag) -->
begin="0s", begin="0.05s", begin="0.1s"
```

#### 3. Modifying Layout

**Resize for different aspect ratios:**
```svg
<!-- 16:9 (current) -->
viewBox="0 0 1920 1080"

<!-- 4:3 -->
viewBox="0 0 1600 1200"

<!-- Square (Instagram) -->
viewBox="0 0 1080 1080"
```

**Reposition panels:**
```svg
<!-- Move left panel -->
<g transform="translate(100, 150)">  <!-- Original -->
<g transform="translate(50, 150)">   <!-- Move left -->
```

#### 4. Adding Data

**Update data points:**
```svg
<!-- Find circles in scatter plots -->
<circle cx="100" cy="150" r="8"/>
<!-- Change position -->
<circle cx="NEW_X" cy="NEW_Y" r="8"/>
```

**Update formulas:**
```svg
<text>θ_new = θ_old − α∇L(θ)</text>
<!-- Replace with your formula -->
<text>YOUR_FORMULA_HERE</text>
```

#### 5. Extending Animations

**Add new elements:**
```svg
<g id="myNewElement" opacity="0">
  <!-- Your content -->
  <animate attributeName="opacity" from="0" to="1"
           begin="YOUR_TIME" dur="0.5s" fill="freeze"/>
</g>
```

**Create loops:**
```svg
<animate attributeName="opacity"
         values="0;1;0" dur="3s"
         repeatCount="indefinite"/>
```

### Editing in Design Tools

#### Figma
1. Import SVG
2. Ungroup to access layers
3. Edit with full fidelity
4. Export back to SVG (preserve IDs)

#### Adobe Illustrator
1. Open SVG
2. Layers panel shows structure
3. Edit visuals
4. Save as SVG (preserve animations)

#### Inkscape
1. Open SVG
2. XML Editor for animations
3. Edit paths/text visually
4. Save as Optimized SVG

### Performance Optimization

**For web display:**
```svg
<!-- Reduce filter complexity -->
<filter id="simpleGlow">
  <feGaussianBlur stdDeviation="2"/>  <!-- Lower value -->
</filter>
```

**For presentations:**
- Keep all animations
- Export as video (ffmpeg) for PowerPoint

**For print:**
- Remove animations
- Increase stroke weights (×1.5)
- Use final state only

---

## Manim Insights Incorporated

### From 3B1B Repository Analysis

**1. Color Philosophy (from custom/colors.py):**
- Blues for mathematical objects
- Reds for emphasis/errors
- Yellows for highlights
- Consistent semantic meaning

**2. Animation Patterns (from scenes):**
```python
# Pattern 1: Progressive build
self.play(FadeIn(title))
self.wait()
self.play(LaggedStartMap(FadeIn, elements))
self.wait()

# Pattern 2: Transform emphasis
self.play(
    ReplacementTransform(old, new),
    old.animate.set_color(YELLOW)
)
```

**3. Visual Encoding (from neural network scenes):**
- Edge thickness = weight magnitude
- Node color = activation value
- Glow intensity = importance
- Motion = information flow

**4. Typography Hierarchy:**
```python
title.scale(1.5)           # 72px equivalent
subtitle.scale(1.0)        # 48px equivalent
label.scale(0.75)          # 36px equivalent
```

**5. Spacing Constants:**
```python
SMALL_BUFF = 0.1
MED_SMALL_BUFF = 0.25
MED_BUFF = 0.5
LARGE_BUFF = 1.0
```

### Key Takeaways

1. **Consistency is paramount** - Use the same colors/styles throughout
2. **Animation guides attention** - Don't animate everything at once
3. **White space is valuable** - Don't fill every pixel
4. **Color carries meaning** - Blue=positive, Red=negative, Yellow=important
5. **Typography matters** - Math notation should be precise
6. **Timing creates narrative** - Fast=excitement, Slow=contemplation

---

## Resources

### 3Blue1Brown Reference
- **Repository:** github.com/3b1b/manim
- **Videos:** youtube.com/@3blue1brown
- **Color constants:** manim/constants.py
- **Animation library:** manim/animation/

### Color Tools
- **Contrast Checker:** webaim.org/resources/contrastchecker
- **Palette Generator:** coolors.co
- **Accessibility:** colorbrewer2.org

### SVG Animation
- **SMIL Reference:** developer.mozilla.org/en-US/docs/Web/SVG/SVG_animation_with_SMIL
- **SVG Filters:** w3.org/TR/SVG/filters.html
- **Animation Examples:** css-tricks.com/guide-svg-animations-smil

### Typography
- **LaTeX Symbols:** detexify.kirelabs.org/classify.html
- **Math Typography:** practicaltypography.com/mathematics.html

---

## Credits & License

**Animations created by:** Claude Code (Anthropic)
**Inspired by:** 3Blue1Brown (Grant Sanderson)
**Style analysis:** Based on official 3b1b/manim repository
**Date:** November 2025

**Usage:**
These animations and this style guide are provided for educational purposes. The 3Blue1Brown visual style is associated with Grant Sanderson's work - please credit appropriately when using similar styling.

**Recommended citation:**
```
"Visualization styled after 3Blue1Brown's educational animations"
```

---

## Version History

**v1.0 (Current):**
- Initial 3B1B-style implementations
- Five core ML animations
- Comprehensive style guide
- Figma-compatible SVG structure

**Planned improvements:**
- Interactive SVG (hover states)
- More transition types
- Additional ML algorithms
- Custom easing functions
- Video export templates

---

*For questions or contributions, refer to the parent project documentation.*
