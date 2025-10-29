# Wits Planetary Health Research Brand Guidelines

## Quick Reference

### Primary Colors

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| **Wits PHR Navy** | `#2c5cda` | 44, 92, 218 | Primary actions, headers, emphasis |
| **Wits PHR Teal** | `#00bec5` | 0, 190, 197 | Secondary accent, data visualization |
| **Wits PHR Blue** | `#20a3fc` | 32, 163, 252 | Tertiary accent, highlights |
| **Wits PHR Red** | `#cc1a1b` | 204, 26, 27 | Critical info, alerts, key findings |

### Neutral Colors

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| **Background Light** | `#f4f4f4` | 244, 244, 244 | Slide backgrounds |
| **Pure White** | `#ffffff` | 255, 255, 255 | Primary canvas |
| **Text Dark** | `#424242` | 66, 66, 66 | Body text |
| **Text Black** | `#1a1a1a` | 26, 26, 26 | Headlines |
| **Text Gray** | `#666666` | 102, 102, 102 | Captions, labels |

### Typography

**Primary Fonts:**
- **Inter** (400, 500, 600, 700) - Body text, labels, captions
- **Roboto** (400, 500, 700) - Headers, subheaders, emphasis

**Font Sizes (1920x1080px slides):**
```
Title:           80-120px (Bold)
Subtitle:        48-64px  (Medium)
Section Header:  56-72px  (SemiBold)
Body Text:       32-40px  (Regular)
Captions:        24-28px  (Regular)
Labels:          28-32px  (Medium)
```

### Layout Standards

**Canvas:** 1920 × 1080px (16:9)
**Margins:** 80-100px all sides
**Grid:** 12 or 24 columns
**Gutters:** 40-60px
**Whitespace:** 40-60% of slide

## Color Palettes

### Data Visualization

**Sequential (light to dark):**
```
#e3ecfc → #b8d4f8 → #8abbe8 → #5c9ed4 → #2c5cda
```

**Categorical (distinct categories):**
```
#2c5cda (Navy)
#00bec5 (Teal)
#20a3fc (Blue)
#cc1a1b (Red)
#55a1ed (Cornflower)
```

**Diverging (cool to warm):**
```
#2c5cda → #5c9ed4 → #8abbe8 → #f4a582 → #cc1a1b
```

## Logo Usage

**Placement:** Bottom right or top right
**Size:** 120-180px width
**Margin:** 40-60px from edges

**Variants:**
- `logo-dark.png` - Use on light backgrounds
- `logo-light-bordered.png` - Use on dark backgrounds

## Design Principles

1. **Clarity over decoration** - Every element serves a purpose
2. **Data-driven storytelling** - Visualize insights effectively
3. **Professional and accessible** - WCAG AA compliance
4. **Scientific rigor** - Accurate representation of data
5. **Consistent brand presence** - Logo and colors on every slide
6. **Figma-editable by default** - Text as text, not paths

## Template Structure

### Standard Slide Components

```
┌─────────────────────────────────────────┐
│  [Title Area]                           │  ← Top 20%
│                                         │
│  [Content Area]                         │  ← Middle 60%
│  (Text, visuals, data)                  │
│                                         │
│                              [Logo]     │  ← Bottom 20%
└─────────────────────────────────────────┘
```

### Visual Hierarchy

1. **Primary:** Title/key message (largest, boldest, top third)
2. **Secondary:** Supporting content (middle, structured)
3. **Tertiary:** Attribution/branding (smallest, bottom corner)

## SVG Best Practices

### Font Import
```svg
<defs>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  </style>
</defs>
```

### Color Classes
```svg
<defs>
  <style>
    .wits-navy { fill: #2c5cda; }
    .wits-teal { fill: #00bec5; }
    .wits-blue { fill: #20a3fc; }
    .wits-red { fill: #cc1a1b; }
    .text-dark { fill: #424242; }
  </style>
</defs>
```

### Layer Organization
```svg
<g id="background">...</g>
<g id="content">...</g>
<g id="branding">...</g>
```

## Accessibility Standards

**Color Contrast:**
- Text on white: #1a1a1a (ratio 16.5:1)
- Text on navy: #ffffff (ensure 4.5:1 minimum)

**Data Visualization:**
- Color blind safe palettes
- Pattern fills as alternative to color
- Direct labels preferred over legends
- High contrast between adjacent elements

## Common Mistakes to Avoid

❌ Converting text to paths (makes uneditable)
❌ Using too many colors (stick to 3-4 per slide)
❌ Cramming content (embrace whitespace)
❌ Small text (<28px body text)
❌ Low contrast combinations
❌ Forgetting the logo
❌ Inconsistent margins
❌ Ungrouped layers in SVG

## Resources

**Fonts:**
- Inter: https://fonts.google.com/specimen/Inter
- Roboto: https://fonts.google.com/specimen/Roboto

**Tools:**
- Figma: https://figma.com (for editing)
- SVGO: https://github.com/svg/svgo (for optimization)

**Organization:**
- Website: https://witsphr.org
- Research focus: Climate change and health

---

**Version:** 1.0
**Last Updated:** 2025-10-29
**Contact:** Data Science Team, Wits Planetary Health Research
