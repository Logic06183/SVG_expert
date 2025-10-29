# SVG Slide Templates

This directory contains production-ready SVG slide templates that demonstrate best practices for Wits Planetary Health Research presentations.

## Template Overview

| Template | File | Best For | Key Features |
|----------|------|----------|--------------|
| **Title Slide** | `01-title-slide.svg` | Opening slides, main titles | Centered layout, gradient accent, clear hierarchy |
| **Content + Visual** | `02-content-with-visual.svg` | Findings with data, balanced layouts | 50/50 split, bullet points, chart area |
| **Full-Width Data** | `03-full-width-data.svg` | Complex charts, detailed visualizations | Bar chart example, gridlines, data labels |
| **Key Message** | `04-key-message.svg` | Critical stats, quotes, major findings | Large central text, minimal design, high impact |
| **Section Header** | `05-section-header.svg` | Section dividers, transitions | Bold section number, gradient accent bar |

## Template Details

### 01 - Title Slide

**Purpose:** Presentation opener, main title screen

**Use When:**
- Starting a presentation
- Introducing a new topic or module
- Conference talk opening

**Layout:**
```
┌─────────────────────────────────────┐
│         [Main Title]                │
│        [Subtitle/Theme]             │
│      [Date/Location/Event]          │
│                              [Logo] │
└─────────────────────────────────────┘
```

**Editable Elements:**
- Main title text
- Subtitle/theme
- Date/location/event
- Accent colors

---

### 02 - Content with Visual

**Purpose:** Balanced text and visualization presentation

**Use When:**
- Presenting findings with supporting data
- Explaining concepts with visual aids
- Comparing qualitative and quantitative information

**Layout:**
```
┌─────────────────────────────────────┐
│  [Title]                            │
│  • Bullet 1     │  [Chart/Visual]   │
│  • Bullet 2     │                   │
│  • Bullet 3     │                   │
│  • Bullet 4     │  [Caption]        │
│                              [Logo] │
└─────────────────────────────────────┘
```

**Editable Elements:**
- Title
- All bullet point text
- Chart/visualization (replace or modify)
- Caption/source

---

### 03 - Full-Width Data

**Purpose:** Detailed data visualization showcase

**Use When:**
- Presenting complex datasets
- Comparing multiple categories
- Highlighting statistical trends
- Data-driven storytelling

**Layout:**
```
┌─────────────────────────────────────┐
│  [Title]                            │
│  [Full-width bar chart with]        │
│  [gridlines, labels, and values]    │
│  [Caption/Key Insight]       [Logo] │
└─────────────────────────────────────┘
```

**Features:**
- Horizontal gridlines for easy reading
- Direct data labels on bars
- Y-axis labels
- Category labels
- Source citation

**Editable Elements:**
- Title
- All bar heights (change data values)
- Data labels
- Category names
- Caption/source

---

### 04 - Key Message

**Purpose:** High-impact statistic or quote presentation

**Use When:**
- Highlighting a single critical finding
- Presenting a powerful statistic
- Emphasizing a key quote
- Creating memorable moments

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│          [HUGE STAT/QUOTE]          │
│         [Supporting text]           │
│            — Source                 │
│                              [Logo] │
└─────────────────────────────────────┘
```

**Features:**
- Extra-large focal text (180px+)
- Minimal distractions
- Decorative circles (subtle)
- Clean, impactful design

**Editable Elements:**
- Main statistic or quote
- Supporting context
- Source attribution
- Accent colors

---

### 05 - Section Header

**Purpose:** Presentation section divider

**Use When:**
- Transitioning between major sections
- Structuring long presentations
- Organizing content into chapters
- Creating visual breaks

**Layout:**
```
┌─────────────────────────────────────┐
│  02                                 │
│  [Section Title]                    │
│  [Brief description]                │
│  ────────                           │
│                              [Logo] │
└─────────────────────────────────────┘
```

**Features:**
- Large section number (bold)
- Gradient accent bar (left edge)
- Background number (watermark effect)
- Clean typography

**Editable Elements:**
- Section number
- Section title
- Description text
- Gradient colors

---

## Using Templates

### Method 1: Direct Editing

1. Open template SVG in a text editor
2. Find the text elements you want to change
3. Replace placeholder text with your content
4. Save and import to Figma

### Method 2: Figma Import & Edit

1. Import template to Figma (File → Import)
2. Double-click text to edit
3. Modify colors and shapes as needed
4. Duplicate and create your slide deck

### Method 3: Request from Claude Code

**Best method** - Use the svg-slide-master skill:

```
Using template 03 (full-width data), create a slide showing
monthly rainfall data for Johannesburg from Jan-Dec 2024
```

The skill will generate a complete, customized slide based on the template structure.

## Customization Tips

### Changing Colors

All templates use CSS classes for colors. Find the `<style>` section and modify:

```svg
<style>
  .accent { fill: #2c5cda; }  /* Change to your color */
  .teal { fill: #00bec5; }
</style>
```

### Adjusting Fonts

Modify font imports in the `<defs>` section:

```svg
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
```

### Resizing Elements

SVG uses coordinates. Common patterns:

```svg
<!-- Text position -->
<text x="960" y="540">Text</text>

<!-- Rectangle -->
<rect x="100" y="100" width="800" height="400"/>

<!-- Circle -->
<circle cx="960" cy="540" r="200"/>
```

Adjust `x`, `y`, `width`, `height`, `cx`, `cy`, `r` values as needed.

## Template Design Principles

All templates follow these principles:

1. **Generous whitespace** (40-60% of slide)
2. **Clear hierarchy** (title → content → branding)
3. **Brand compliance** (Wits PHR colors and fonts)
4. **Figma compatibility** (text as text, not paths)
5. **Accessibility** (WCAG AA contrast ratios)
6. **Professional quality** (publication-ready)

## Creating Your Own Templates

To create a new template:

1. Start with the base structure:
   ```svg
   <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080">
     <defs><style>/* styles */</style></defs>
     <g id="background">...</g>
     <g id="content">...</g>
     <g id="branding">...</g>
   </svg>
   ```

2. Follow layout standards:
   - Canvas: 1920×1080px
   - Margins: 80-100px
   - Brand colors from `branding/wits-phr-brand-config.json`

3. Test in Figma:
   - Import and verify editability
   - Check layer organization
   - Ensure text is selectable

4. Document:
   - Add to this README
   - Include usage examples
   - Note any special features

## Quick Reference: Which Template?

| Content Type | Use Template | Example |
|--------------|--------------|---------|
| Presentation opener | 01 - Title | "Climate Change & Health: A South African Perspective" |
| Findings + chart | 02 - Content + Visual | "Key Findings" with 4 bullets and bar chart |
| Detailed data | 03 - Full-Width Data | Temperature trends across regions |
| Critical stat | 04 - Key Message | "68% of children affected" |
| Section break | 05 - Section | "02 - Methodology" divider |

## Need Help?

- **Brand questions:** See `branding/BRAND_GUIDE.md`
- **Technical SVG:** See `.claude/skills/svg-slide-master.md`
- **Usage guide:** See main `README.md`
- **Examples:** Request slides using the Claude Code skill

---

**All templates are Figma-ready and brand-compliant.**

Start with a template, customize in Figma, create exceptional presentations.
