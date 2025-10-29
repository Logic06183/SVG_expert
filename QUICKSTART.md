# Quick Start Guide

Get up and running with the SVG Slide Master in 5 minutes.

## Step 1: Activate the Skill (30 seconds)

The `svg-slide-master` skill is ready to use in this repository. No configuration needed!

## Step 2: Request Your First Slide (1 minute)

Try this example:

```
Create a title slide for "Climate Resilience in Urban Areas"
with subtitle "Community-Based Adaptation Strategies"
and today's date
```

Claude Code will generate a complete, brand-compliant SVG slide.

## Step 3: Save the SVG (15 seconds)

When Claude Code outputs the SVG code, save it to a file:

```bash
# Save as my-slide.svg
```

Or copy the code and save it manually.

## Step 4: Import to Figma (2 minutes)

1. Open Figma (https://figma.com)
2. Click **File → Import**
3. Select your `my-slide.svg` file
4. Done! Your slide is now fully editable

## Step 5: Customize (1 minute)

In Figma:
- Double-click any text to edit it
- Click shapes/colors to change them
- Drag elements to reposition
- Export as PNG, PDF, or SVG

---

## Common Requests

### Title Slide
```
Make a title slide for my presentation on heat exposure and health outcomes,
include my name and affiliation
```

### Data Visualization
```
Create a bar chart slide comparing malaria cases in 5 provinces:
Gauteng (1200), KZN (1800), Limpopo (2100), Mpumalanga (950), North West (730)
```

### Key Statistic
```
Generate a key message slide highlighting that 2.4 million people
are at risk from climate-related health impacts in South Africa
```

### Content Slide
```
Make a slide titled "Risk Factors" with 4 bullet points:
- Rising temperatures increase vector breeding
- Urban heat islands amplify exposure
- Vulnerable populations disproportionately affected
- Infrastructure gaps reduce adaptive capacity

Include a simple icon or visual on the right side
```

---

## Tips for Best Results

### ✅ Do This

- **Be specific** about content and data
- **Mention the template** if you have a preference (e.g., "use template 3")
- **Include actual data** for charts (numbers, categories)
- **Specify colors** if you want specific brand colors (navy, teal, blue, red)

### ❌ Avoid This

- Vague requests like "make a slide"
- Requesting features incompatible with SVG/Figma
- Forgetting to specify data for charts
- Asking for animated or interactive elements (SVG is static)

---

## Your First 3 Slides

Let's build a mini presentation:

### Slide 1: Title
```
Create a title slide:
Title: "Climate Change and Vector-Borne Diseases"
Subtitle: "Evidence from Southern Africa"
Date: [Today's date]
```

### Slide 2: Key Finding
```
Generate a key message slide with the statistic:
"3.2× increase in malaria transmission risk"
Context: "Per 1°C warming above baseline"
Source: "Wits PHR Climate Health Study, 2024"
```

### Slide 3: Data Comparison
```
Create a data visualization slide comparing projected temperature
increases by 2050 across regions:
- Coastal: +1.8°C
- Inland: +2.4°C
- Northern: +2.7°C
Use horizontal bars, navy color, include gridlines
```

Save these three slides, import to Figma, and you have the start of a presentation!

---

## Keyboard Shortcuts (Figma)

Once your slides are in Figma:

- **T** - Text tool (edit text)
- **R** - Rectangle tool
- **O** - Oval tool
- **Cmd/Ctrl + D** - Duplicate
- **Cmd/Ctrl + G** - Group
- **Cmd/Ctrl + Shift + E** - Export

---

## Next Steps

### Explore Templates

Check out the 5 included templates:

```bash
open templates/
```

Each template shows a different layout style.

### Read the Brand Guide

Understand Wits PHR colors and fonts:

```bash
open branding/BRAND_GUIDE.md
```

### Review Full Documentation

For advanced usage and customization:

```bash
open README.md
```

---

## Troubleshooting

### "The skill isn't working"

Make sure you're in the SVG_expert directory when using Claude Code:

```bash
cd "/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert"
```

### "Fonts look different in Figma"

Figma needs to download fonts. Check your internet connection, or install Inter and Roboto locally:
- Inter: https://fonts.google.com/specimen/Inter
- Roboto: https://fonts.google.com/specimen/Roboto

### "Text is not editable"

This shouldn't happen with the skill, but if it does:
- The SVG may have been exported incorrectly
- Re-generate the slide using the skill
- Ensure text is `<text>` elements, not `<path>` in the SVG

### "Colors don't match"

Check your color profile:
- Figma should use sRGB
- Export settings should match
- Verify hex codes: Navy `#2c5cda`, Teal `#00bec5`, Blue `#20a3fc`, Red `#cc1a1b`

---

## Example Workflow

**Real-world scenario:** You need 10 slides for a conference presentation tomorrow.

### Step 1: Plan Your Slides (10 min)
1. Title slide
2. Background/context
3. Research question
4. Methodology
5. Data overview
6. Key finding 1 (with chart)
7. Key finding 2 (with chart)
8. Implications
9. Recommendations
10. Thank you/contact

### Step 2: Generate Slides (30 min)

Request each slide from Claude Code:

```
Generate slide 1: title slide for [your title]
Generate slide 2: content slide titled "Background" with 4 bullets about [context]
Generate slide 3: key message slide with research question: "[your question]"
...continue for all 10 slides
```

Save each SVG as `slide-01.svg`, `slide-02.svg`, etc.

### Step 3: Import to Figma (10 min)

- Import all 10 SVGs to Figma
- Arrange on pages or frames
- Quick review for consistency

### Step 4: Finalize (30 min)

- Edit any text for clarity
- Adjust colors if needed
- Add presenter notes (Figma comments)
- Export final versions

### Step 5: Present! (20 min)

Export as PDF or PNG sequence, upload to presentation software, deliver with confidence.

**Total time:** ~2 hours for a complete, professional presentation

---

## Resources at a Glance

| Resource | Location | Purpose |
|----------|----------|---------|
| **Skill File** | `.claude/skills/svg-slide-master.md` | Complete skill reference |
| **Brand Guide** | `branding/BRAND_GUIDE.md` | Colors, fonts, guidelines |
| **Templates** | `templates/` | 5 ready-to-use examples |
| **Full Docs** | `README.md` | Comprehensive documentation |

---

## You're Ready!

Start generating exceptional slides. The skill is optimized to understand:
- Research presentation needs
- Climate and health context
- Data visualization requirements
- Academic and professional standards

**Your first request should take less than 30 seconds to generate a production-ready slide.**

Go ahead, try it now!

```
Create a title slide for my next presentation
```

---

**Questions?** Review the main README.md or consult the brand guide.

**Issues?** The skill is designed to be forgiving - just describe what you need in plain language.

**Improvements?** Save your favorite slides as templates for future use.

---

Built for **Wits Planetary Health Research**
Optimized for **speed, quality, and brand compliance**
Ready for **Figma editing and professional presentations**

🚀 Start creating!
