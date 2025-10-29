# Example Slides - SHAP Environmental Health Case Study

This folder contains real-world example slides demonstrating the SVG Slide Master skill applied to actual research content about SHAP (SHapley Additive exPlanations) analysis in environmental health.

## Content Source

These examples are based on research about machine learning prediction models using SHAP interpretation for chronic bronchitis risk assessment based on heavy metal exposure, using a nationally representative sample of 7,493 participants.

**Citation:** BMC Pulmonary Medicine, 2025 | DOI: 10.1186/s12890-025-03724-8

## Examples Included

### 1. Full Comprehensive Slide
**File:** `shap-environmental-health-full.svg`

**Type:** Two-column detailed content slide

**Features:**
- Complete research summary with dual-column layout
- Left column: Key Findings (study design, ML model, SHAP rankings, insights)
- Right column: Relevance to Your Work (environmental exposome, dose-response, screening)
- Highlighted application box with pipeline recommendations
- Full citation footer
- Color-coded sections with Wits PHR branding

**Use When:**
- Presenting comprehensive research summaries
- Journal club presentations
- Detailed literature reviews
- Grant proposals showing methodology parallels

**Layout Lessons:**
- Two equal columns for balanced information
- Section headers with gradient backgrounds
- Color-coded importance (red for top finding, gold for secondary)
- Highlight boxes for key takeaways
- Consistent bullet styling throughout

---

### 2. Key Finding Highlight
**File:** `shap-key-finding.svg`

**Type:** Impact statistic slide (Template 04 variant)

**Features:**
- Large "#1" as hero element
- Focus on blood-cadmium as strongest predictor
- Minimal design for maximum impact
- Subtle decorative circles
- Clear context and citation

**Use When:**
- Emphasizing a single critical finding
- Conference presentations (attention-grabbing)
- Social media graphics
- Executive summaries

**Layout Lessons:**
- Hero number at 180px font size
- Generous whitespace (60%+)
- Supporting text in hierarchy below
- Decorative elements at 6% opacity
- Color reinforces message (red for #1 importance)

---

### 3. Feature Ranking Visualization
**File:** `shap-feature-ranking.svg`

**Type:** Data visualization slide (Template 03 variant)

**Features:**
- Horizontal bar chart showing SHAP values
- Color-gradient bars (red→gold→blue)
- Direct data labels on bars
- Annotation for strongest predictor
- Clean gridlines and axis labels

**Use When:**
- Presenting model results
- Comparing variable importance
- Data-driven decision making
- Quantitative findings

**Layout Lessons:**
- Bars sorted by magnitude (largest first)
- Color gradient indicates importance
- Direct labels eliminate need for legend
- Annotation draws attention to key finding
- Y-axis labels right-aligned for readability

---

### 4. Methodology Flow
**File:** `shap-methodology-flow.svg`

**Type:** Process/workflow diagram

**Features:**
- 4-step numbered process flow
- Circular number badges with gradients
- Connected with arrows showing progression
- Each step has title, description, and notes
- Application insight box
- Color progression through workflow

**Use When:**
- Explaining research methodology
- Teaching analytical workflows
- Process documentation
- Proposal methodology sections

**Layout Lessons:**
- Sequential layout (left-to-right, then down)
- Consistent card sizing (320×300px)
- Number badges stand out with gradients
- Arrows show flow direction
- Highlight boxes for additional context
- Different colors for each step aid memory

---

## Design Principles Demonstrated

### 1. Information Hierarchy
All examples show clear visual hierarchy:
- Primary message (largest, boldest)
- Supporting details (medium)
- Metadata/citations (smallest)

### 2. Color Strategy
- **Red (#cc1a1b):** Critical findings, strongest predictors
- **Gold (#d68910):** Secondary importance, warnings
- **Blue (#2c5cda):** Standard Wits PHR primary
- **Teal (#00bec5):** Secondary accents
- **Orange (#e67e22):** Subject-specific accent (environmental health)

### 3. Typography
- **Inter font family** throughout
- **Weight variation** for emphasis (400, 500, 600, 700)
- **Size hierarchy** strictly maintained
- **Line height** optimized for readability (1.4-1.6 for body)

### 4. Layout
- **Margins:** 100px minimum from edges
- **Whitespace:** 40-60% of slide area
- **Alignment:** Consistent throughout
- **Balance:** Visual weight distributed evenly

### 5. Accessibility
- **Color contrast:** WCAG AA compliant
- **Text size:** Minimum 15px for body text
- **Direct labels:** Charts have values, not just legends
- **Clear structure:** Logical reading order

## Technical Notes

### Figma Compatibility
All examples are fully Figma-editable:
- ✅ Text as `<text>` elements (not paths)
- ✅ Named layer groups (`id` attributes)
- ✅ CSS classes for consistent styling
- ✅ Semantic shapes (rect, circle, line)
- ✅ Gradients defined in `<defs>`

### File Sizes
- Full comprehensive: ~15 KB
- Key finding: ~6 KB
- Feature ranking: ~10 KB
- Methodology flow: ~12 KB

All well within optimal range (<500 KB).

### Font Loading
All examples import Inter from Google Fonts:
```svg
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
```

Requires internet connection on first load, then cached.

## Using These Examples

### As Templates
1. Open in text editor
2. Find and replace content text
3. Adjust colors if needed
4. Save and import to Figma

### As Learning Tools
- Study the layer structure
- Examine color usage
- Note typography choices
- Analyze layout decisions

### As Starting Points
- Copy structure for similar content
- Adapt layout to your data
- Maintain brand consistency
- Follow established patterns

## Customization Ideas

### Full Comprehensive Slide
- Adapt to 3-column layout for more topics
- Change section colors for different subjects
- Add more bullet points (up to 5-6 per section)
- Replace citation footer with acknowledgments

### Key Finding Highlight
- Change number to percentage or statistic
- Swap red accent for blue (positive findings)
- Add small supporting icons
- Multiple key findings (2-3) in grid

### Feature Ranking
- Flip to vertical bars for categories
- Add confidence intervals
- Group bars by category
- Extend to 8-10 features

### Methodology Flow
- Add 5th or 6th step
- Branch into parallel processes
- Add decision points (diamonds)
- Integrate with other diagrams

## Related Content

**Research Application:**
These examples demonstrate how SHAP analysis in environmental health mirrors climate-health research approaches at Wits PHR. The methodology is directly transferable to:

- Climate exposure analysis
- Preterm birth risk modeling
- Multi-exposure environmental health studies
- Machine learning interpretation in epidemiology

## Questions Answered

### Why these examples?
They represent **real research** that's relevant to Wits PHR's climate-health focus, demonstrating practical application of the slide templates.

### Why multiple versions?
Different presentation contexts require different approaches:
- **Full slide:** Comprehensive review, detailed analysis
- **Key finding:** Conference talks, quick impact
- **Data viz:** Results presentation, quantitative focus
- **Methodology:** Teaching, proposals, documentation

### Can I combine them?
Absolutely! These examples can be sequenced in a presentation:
1. Methodology flow (context)
2. Feature ranking (results)
3. Key finding (impact)
4. Full comprehensive (implications)

## Best Practices from Examples

1. **Start with structure** - Clear sections with headers
2. **Use color meaningfully** - Not just decoration
3. **Guide the eye** - Visual flow through content
4. **Label directly** - Don't make viewers hunt for meaning
5. **Cite sources** - Always include references
6. **Brand consistently** - Logo/attribution on every slide

## Next Steps

1. **Open in Figma** - Import and explore editability
2. **Modify content** - Practice with your own data
3. **Create variations** - Try different color schemes
4. **Build sequences** - Combine into presentations
5. **Share feedback** - What works? What doesn't?

---

**These examples showcase the SVG Slide Master skill at its best:**
- Professional quality
- Figma-ready
- Brand-compliant
- Content-rich
- Visually clear
- Technically sound

Use them as inspiration, templates, or learning tools for your own presentation needs.

---

**Created for Wits Planetary Health Research**
Demonstrating excellence in scientific communication design.
