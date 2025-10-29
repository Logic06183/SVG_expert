# Wits Planetary Health Research - SVG Slide Master

Professional, Figma-ready SVG slide generation for climate and health research presentations.

## Overview

This repository contains an exceptional Claude Code skill for generating publication-quality SVG slides that import flawlessly into Figma with fully editable layers. Optimized for Wits Planetary Health Research branding and visual identity.

## Features

- **One-shot slide generation** - Request a slide, get production-ready SVG
- **Figma-optimized** - All text remains editable, layers properly organized
- **Brand-compliant** - Wits PHR colors, fonts, and style guidelines built-in
- **Multiple templates** - Title, content, data visualization, key messages, sections
- **Professional quality** - Publication-ready output every time
- **Accessibility-first** - WCAG AA compliant color contrast and readability

## Quick Start

### 1. Activate the Skill

In Claude Code, the `svg-slide-master` skill is automatically available. Simply request a slide:

```
Generate a title slide for my presentation on climate change and malaria
```

```
Create a data visualization slide showing temperature trends across Africa
```

```
Make a key message slide highlighting that 2.4°C warming is projected by 2100
```

### 2. Import to Figma

1. Save the generated SVG file (e.g., `my-slide.svg`)
2. In Figma: **File → Import**
3. Select your SVG file
4. All layers are now editable - text, colors, shapes

### 3. Customize

- Double-click any text to edit
- Select elements to change colors
- Reorganize layers in the Layers panel
- Export as PNG, PDF, or keep as SVG

## Repository Structure

```
.
├── .claude/
│   └── skills/
│       └── svg-slide-master.md     # Main skill file
├── branding/
│   ├── BRAND_GUIDE.md              # Quick reference guide
│   └── wits-phr-brand-config.json  # Complete brand specifications
├── templates/
│   ├── 01-title-slide.svg          # Title slide template
│   ├── 02-content-with-visual.svg  # 50/50 text/visual layout
│   ├── 03-full-width-data.svg      # Full-width chart template
│   ├── 04-key-message.svg          # Key stat/quote highlight
│   ├── 05-section-header.svg       # Section divider template
│   ├── examples/                   # Real-world examples
│   │   ├── shap-environmental-health-full.svg
│   │   ├── shap-key-finding.svg
│   │   ├── shap-feature-ranking.svg
│   │   ├── shap-methodology-flow.svg
│   │   └── README.md               # Examples documentation
│   └── README.md                   # Template guide
├── README.md                        # This file
├── QUICKSTART.md                   # 5-minute getting started
├── EXAMPLES.md                     # Usage examples
└── VALIDATION.md                   # Testing guide
```

## Templates

### 1. Title Slide
Use for: Opening slides, main title screens

**Structure:**
- Centered title (large, bold)
- Subtitle/theme (medium)
- Date/location/event (small)
- Logo in bottom right

### 2. Content with Visual
Use for: Key findings with supporting chart, balanced text/visual

**Structure:**
- Title at top
- Left: Bullet points or text (50%)
- Right: Visualization or image (50%)
- Caption/source at bottom

### 3. Full-Width Data
Use for: Complex charts, detailed visualizations, data-driven slides

**Structure:**
- Title at top
- Full-width chart (bar, line, etc.)
- Caption with key insight and source
- Gridlines and labels

### 4. Key Message
Use for: Critical statistics, quotes, major findings

**Structure:**
- Huge central number or quote (180px+)
- Supporting context below
- Source citation
- Minimal decorative elements

### 5. Section Header
Use for: Dividing presentation sections, transitions

**Structure:**
- Large section number
- Section title (bold)
- Brief description
- Accent bar or decorative element

## Branding Guidelines

### Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Wits PHR Navy** | `#2c5cda` | Primary emphasis |
| **Wits PHR Teal** | `#00bec5` | Secondary accent |
| **Wits PHR Blue** | `#20a3fc` | Tertiary accent |
| **Wits PHR Red** | `#cc1a1b` | Critical info |

### Typography

- **Primary:** Inter (400, 500, 600, 700)
- **Secondary:** Roboto (400, 500, 700)
- **Sizes:** 80-120px (titles), 32-40px (body), 24-28px (captions)

### Layout

- **Canvas:** 1920×1080px (16:9)
- **Margins:** 80-100px all sides
- **Whitespace:** 40-60% of slide

See [`branding/BRAND_GUIDE.md`](branding/BRAND_GUIDE.md) for complete guidelines.

## Real-World Examples

The `templates/examples/` directory contains professional examples based on actual research:

### SHAP Environmental Health Case Study

Four complete slides demonstrating different approaches to presenting research about SHAP (SHapley Additive exPlanations) analysis for chronic bronchitis risk from heavy metal exposure:

1. **Comprehensive Full Slide** (`shap-environmental-health-full.svg`)
   - Two-column layout with Key Findings and Relevance sections
   - 15 KB, highly detailed, perfect for literature reviews
   - Shows color-coding, highlight boxes, structured content

2. **Key Finding Highlight** (`shap-key-finding.svg`)
   - Impact slide emphasizing "#1 SHAP-Ranked Feature"
   - 3.2 KB, minimal design, maximum impact
   - Template 04 style (key message)

3. **Feature Ranking Visualization** (`shap-feature-ranking.svg`)
   - Horizontal bar chart showing SHAP importance values
   - 6.2 KB, data-driven, clear visual hierarchy
   - Template 03 style (full-width data)

4. **Methodology Flow** (`shap-methodology-flow.svg`)
   - 4-step process diagram with numbered badges
   - 8.5 KB, educational, process documentation
   - Custom workflow layout

**Why these examples?** They demonstrate real research content relevant to Wits PHR's climate-health focus, showing how the templates adapt to complex academic material.

**See [`templates/examples/README.md`](templates/examples/README.md) for detailed breakdowns of each example.**

## Usage Examples

### Example 1: Research Findings

**Request:**
> Create a slide showing our key findings on heat exposure and hospital admissions. Include 4 bullet points on the left and a bar chart on the right.

**Output:** Content with Visual template, Wits colors, proper spacing, Figma-editable layers.

### Example 2: Statistical Highlight

**Request:**
> Make a slide highlighting that 68% of climate-related health impacts in Africa affect children under 5.

**Output:** Key Message template, large percentage, context text, source citation.

### Example 3: Methodology Section

**Request:**
> Create a section divider slide for our Methodology section, with section number 03.

**Output:** Section Header template, "03" prominently displayed, clean design.

## Advanced Usage

### Custom Requests

The skill handles complex requirements:

```
Generate a slide with:
- Title: "Urban Heat Island Effect"
- 3 bullet points about UHI causes
- A donut chart showing land use breakdown (60% built, 25% vegetation, 15% other)
- Use teal as the primary accent color
```

### Data Visualization

Request specific chart types:

```
Create a line chart slide showing temperature trends from 2000-2024
with three lines: Africa (navy), Asia (teal), Global average (blue)
```

### Iterative Refinement

If you need adjustments:

```
Adjust the previous slide to:
- Make the title larger
- Add a gradient background
- Change the bars to horizontal orientation
```

## Technical Details

### SVG Structure

Generated SVGs follow best practices:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
  <defs>
    <style>
      /* Font imports and CSS classes */
    </style>
  </defs>

  <g id="background">...</g>
  <g id="content">...</g>
  <g id="branding">...</g>
</svg>
```

### Figma Compatibility

- ✅ Text as `<text>` elements (not paths)
- ✅ Named layers with `id` attributes
- ✅ Logical grouping with `<g>` tags
- ✅ CSS classes for consistent styling
- ✅ Semantic shapes (rect, circle, line)
- ✅ Optimized file size (<500KB)

### Font Handling

Fonts are imported via Google Fonts:

```svg
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
```

This ensures consistent rendering across platforms.

## Best Practices

### When Requesting Slides

**Be specific about:**
- Slide purpose (title, data, message)
- Content to include (text, data, visuals)
- Preferred template or layout
- Any special requirements

**Good requests:**
```
✅ "Create a title slide for 'Climate Change and Vector-Borne Diseases'
    with subtitle 'A South African Perspective' and today's date"

✅ "Make a data slide comparing malaria cases across 5 provinces,
    use a bar chart, include the data labels"

✅ "Generate a key message slide: '3.2 million people affected'
    with context about heat-related illnesses"
```

**Less effective:**
```
❌ "Make a slide"
❌ "Create something about climate"
❌ "I need a chart"
```

### Editing in Figma

1. **Organize layers** - Use the Layers panel to find specific elements
2. **Group related items** - Keep content organized
3. **Use components** - For repeated elements (logos, etc.)
4. **Export settings** - PNG at 2x for presentations, PDF for print

### Accessibility

- Ensure minimum 4.5:1 contrast ratio for text
- Use direct labels on charts, not just legends
- Provide alt text when exporting to other formats
- Test color-blind friendliness (use provided palettes)

## Customization

### Modifying the Skill

The skill file is located at `.claude/skills/svg-slide-master.md`. You can:

- Add new templates
- Adjust default colors
- Change font preferences
- Add organization-specific guidelines

### Adding New Templates

1. Create SVG file in `templates/`
2. Follow existing structure (background, content, branding layers)
3. Use brand colors and fonts
4. Document in this README

## Troubleshooting

### Text Not Editable in Figma

**Issue:** Text appears as shapes, not editable text.

**Solution:** Ensure text is created with `<text>` elements, not `<path>`. The skill does this automatically, but if manually editing, verify the structure.

### Fonts Not Displaying

**Issue:** Fonts show as fallbacks (Arial, etc.)

**Solution:**
1. Check internet connection (fonts load from Google Fonts)
2. Install fonts locally if offline work is needed
3. Use font substitution in Figma if necessary

### File Size Too Large

**Issue:** SVG file is several MB.

**Solution:**
- Avoid embedding images as base64 (link externally instead)
- Simplify complex paths
- Use SVGO for optimization: `svgo input.svg -o output.svg`

### Colors Don't Match Brand

**Issue:** Colors look different from brand guidelines.

**Solution:**
- Check display color profile (use sRGB)
- Verify hex codes match `branding/wits-phr-brand-config.json`
- Regenerate with explicit color specifications

## Resources

### Wits Planetary Health Research

- **Website:** https://witsphr.org
- **Focus:** Climate change and health research
- **Location:** Johannesburg, South Africa

### Tools & References

- **Figma:** https://figma.com (for editing SVGs)
- **Inter Font:** https://fonts.google.com/specimen/Inter
- **Roboto Font:** https://fonts.google.com/specimen/Roboto
- **SVGO:** https://github.com/svg/svgo (for optimization)
- **WCAG Guidelines:** https://www.w3.org/WAI/WCAG21/quickref/

### Learning Resources

- **SVG Tutorial:** https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial
- **Figma Docs:** https://help.figma.com
- **Data Viz Best Practices:** https://www.storytellingwithdata.com

## Contributing

This is a personal/team repository. To suggest improvements:

1. Test your changes thoroughly
2. Ensure brand compliance
3. Update documentation
4. Share with the team for review

## Version History

- **v1.0** (2025-10-29)
  - Initial release
  - 5 core templates
  - Complete Wits PHR branding
  - Figma-optimized SVG generation
  - Comprehensive documentation

## License

This repository contains branding materials for Wits Planetary Health Research. Please ensure proper authorization before using these assets for external projects.

---

## Getting Started Checklist

- [ ] Review brand guidelines in `branding/BRAND_GUIDE.md`
- [ ] Explore example templates in `templates/`
- [ ] Test the skill with a simple request
- [ ] Import a generated SVG into Figma
- [ ] Customize and export your first slide
- [ ] Share with your team!

## Support

For questions or issues:

1. Check this README and brand guide
2. Review example templates
3. Consult the skill file for technical details
4. Contact the Wits PHR Data Science team

---

**Built for excellence. Designed for Wits Planetary Health Research.**

Generate slides that set the standard. 🌍
