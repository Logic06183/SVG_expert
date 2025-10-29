# SVG Slide Master Validation Guide

Quick tests to verify the skill is working correctly and producing high-quality output.

## Quick Validation Tests

### Test 1: Basic Functionality (2 minutes)

**Request:**
```
Create a simple title slide with "Test Presentation" as the title
```

**Expected Output:**
- ✅ Valid SVG syntax
- ✅ 1920×1080px viewBox
- ✅ Wits PHR branding colors present
- ✅ Text as `<text>` elements (not paths)
- ✅ Proper layer grouping (background, content, branding)

**Validation Steps:**
1. Check SVG opens in browser without errors
2. Text should be selectable in browser
3. Import to Figma works without warnings
4. Text is editable in Figma

---

### Test 2: Brand Compliance (3 minutes)

**Request:**
```
Create a data visualization slide showing 3 bars with values 100, 150, 200
Use Wits PHR brand colors
```

**Expected Colors:**
- ✅ Navy: `#2c5cda`
- ✅ Teal: `#00bec5`
- ✅ Blue: `#20a3fc`
- ✅ Text: `#424242` or `#1a1a1a`

**Validation Steps:**
1. Inspect SVG code for hex values
2. Match against `branding/wits-phr-brand-config.json`
3. Visual inspection - colors should look professional and consistent

---

### Test 3: Figma Editability (5 minutes)

**Request:**
```
Generate a content slide with a title and 4 bullet points
```

**Expected Editability:**
- ✅ All text is directly editable (double-click works)
- ✅ Layers are named and organized
- ✅ Fonts load correctly (Inter/Roboto)
- ✅ Elements can be selected and moved
- ✅ Colors can be changed via fill property

**Validation Steps:**
1. Import to Figma
2. Double-click title - should allow editing
3. Check Layers panel - should see "background", "content", "branding" groups
4. Try changing a color - should be straightforward
5. Try moving an element - should work without breaking layout

---

### Test 4: Complex Data Visualization (7 minutes)

**Request:**
```
Create a bar chart slide with 5 categories and gridlines:
A: 45, B: 78, C: 63, D: 91, E: 52
Include axis labels and data labels on bars
```

**Expected Elements:**
- ✅ Bars proportional to data values
- ✅ Gridlines present and subtle
- ✅ Y-axis labels
- ✅ X-axis category labels
- ✅ Data labels on or above bars
- ✅ Clear title and caption

**Validation Steps:**
1. Visual inspection - chart should be readable
2. Check proportions - bars should scale correctly
3. Verify all labels are present
4. Import to Figma - all elements editable

---

### Test 5: Typography Standards (5 minutes)

**Request:**
```
Create a slide with title, subtitle, body text, and caption to test typography
```

**Expected Hierarchy:**
- ✅ Title: 80-120px, bold
- ✅ Subtitle: 48-64px, medium
- ✅ Body: 32-40px, regular
- ✅ Caption: 24-28px, regular

**Validation Steps:**
1. Inspect SVG - check `font-size` attributes
2. Visual hierarchy should be immediately clear
3. Line heights appropriate (1.1-1.2 for titles, 1.4-1.6 for body)
4. Letter spacing on large text (-0.02em)

---

## Comprehensive Checklist

Use this checklist for any generated slide:

### SVG Structure
- [ ] Valid XML syntax (no errors)
- [ ] Correct namespace: `xmlns="http://www.w3.org/2000/svg"`
- [ ] ViewBox: `0 0 1920 1080`
- [ ] Width/height: `1920` × `1080`

### Layer Organization
- [ ] Contains `<g id="background">` group
- [ ] Contains `<g id="content">` group
- [ ] Contains `<g id="branding">` group
- [ ] Nested groups have descriptive IDs

### Typography
- [ ] Font imports in `<defs><style>` section
- [ ] Text uses `<text>` elements (NOT `<path>`)
- [ ] Font family specified (Inter or Roboto)
- [ ] Font sizes follow hierarchy
- [ ] Line heights appropriate

### Colors
- [ ] Uses Wits PHR brand palette
- [ ] High contrast (WCAG AA minimum)
- [ ] Consistent across elements
- [ ] CSS classes defined for colors

### Layout
- [ ] Adequate margins (80-100px)
- [ ] Elements properly aligned
- [ ] Generous whitespace (40-60%)
- [ ] Clear visual hierarchy

### Branding
- [ ] Logo area or text branding present
- [ ] Positioned correctly (bottom-right or top-right)
- [ ] Appropriate size and opacity

### Figma Compatibility
- [ ] Imports without errors
- [ ] All text is editable
- [ ] Layers are selectable
- [ ] No unexpected groupings or flattening

### Quality
- [ ] Professional appearance
- [ ] Readable at presentation size
- [ ] Consistent with brand standards
- [ ] No spelling/grammar errors in template text

---

## Common Issues & Solutions

### Issue: Text Not Editable in Figma

**Symptoms:** Text appears as shapes, can't be edited

**Check:**
```svg
<!-- ❌ Wrong (converted to path) -->
<path d="M123.4,567.8 L..."/>

<!-- ✅ Correct (text element) -->
<text x="100" y="150">Text Here</text>
```

**Solution:** Regenerate slide, skill should always use `<text>` elements

---

### Issue: Colors Don't Match Brand

**Symptoms:** Colors look wrong or inconsistent

**Check:**
```svg
<defs>
  <style>
    .wits-navy { fill: #2c5cda; }  /* Should be exact hex */
  </style>
</defs>
```

**Solution:** Verify hex codes match `branding/wits-phr-brand-config.json`, adjust if needed

---

### Issue: Layout Broken in Figma

**Symptoms:** Elements overlap or appear misaligned

**Check:**
- ViewBox should be `0 0 1920 1080`
- Coordinates should be within canvas
- No transforms that break layout

**Solution:** Review coordinates, ensure all elements within margins

---

### Issue: Fonts Not Loading

**Symptoms:** Fonts fallback to Arial/Helvetica

**Check:**
```svg
<defs>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  </style>
</defs>
```

**Solution:**
1. Verify internet connection
2. Install fonts locally if offline
3. Check font import URL is accessible

---

### Issue: File Size Too Large

**Symptoms:** SVG file is several MB

**Check:**
- No embedded images as base64
- No unnecessary decimal precision
- No complex filters or effects

**Solution:**
```bash
# Optimize with SVGO
svgo input.svg -o output.svg --multipass
```

---

## Performance Benchmarks

Expected generation times and file sizes:

| Slide Type | Generation Time | Typical File Size |
|------------|-----------------|-------------------|
| Title Slide | <5 seconds | 5-10 KB |
| Content Slide | <10 seconds | 10-20 KB |
| Simple Chart | <15 seconds | 15-30 KB |
| Complex Chart | <30 seconds | 30-60 KB |
| Multi-element | <45 seconds | 40-100 KB |

If generation takes significantly longer or files are much larger, investigate complexity and optimize.

---

## Quality Assurance Workflow

### For Individual Slides

1. **Generate** - Request slide from skill
2. **Inspect** - Review SVG code for structure
3. **Validate** - Run through checklist
4. **Import** - Test in Figma
5. **Edit** - Verify all elements editable
6. **Approve** - Sign off on quality

### For Presentation Decks

1. **Plan** - Outline all slides needed
2. **Generate** - Create all slides in batch
3. **Import** - Bring all into Figma
4. **Review** - Check consistency across slides
5. **Edit** - Make final adjustments
6. **Export** - Prepare for presentation

---

## Regression Testing

If modifying the skill file, test these scenarios:

### Test Suite

1. **Basic Shapes**
   - Request: "Create a slide with a rectangle, circle, and line"
   - Verify: All shapes render correctly

2. **Text Elements**
   - Request: "Create a slide with title, subtitle, body, and caption"
   - Verify: All text hierarchy correct

3. **Colors**
   - Request: "Use all 4 Wits PHR primary colors in a slide"
   - Verify: Navy, teal, blue, red all present and correct

4. **Data Viz**
   - Request: "Create a bar chart with 3 bars"
   - Verify: Bars proportional, labels present

5. **Layout**
   - Request: "Create a 50/50 split layout slide"
   - Verify: Equal columns, proper alignment

6. **Branding**
   - Request: "Include branding on a title slide"
   - Verify: Logo area or text present in correct location

---

## Acceptance Criteria

Before considering the skill "production-ready", ensure:

- [ ] All 5 quick validation tests pass
- [ ] Comprehensive checklist items met
- [ ] No common issues present
- [ ] Performance benchmarks achieved
- [ ] Test suite passes 100%
- [ ] Multiple slides can be generated consistently
- [ ] Figma import works reliably
- [ ] Brand compliance verified
- [ ] Typography standards followed
- [ ] Layout quality professional

---

## Continuous Validation

### Weekly Quick Check (5 minutes)

Generate one test slide per week to ensure skill remains functional:

```
Create a test slide with today's date and a simple bar chart
```

Verify:
- Still generates correctly
- Colors unchanged
- Figma import works
- No degradation in quality

### Monthly Deep Check (30 minutes)

Run full test suite:
1. All 5 quick validation tests
2. Generate one of each template type
3. Create a complex multi-element slide
4. Import all to Figma
5. Document any issues

---

## Reporting Issues

If validation fails, document:

1. **What was requested** (exact prompt)
2. **What was expected** (based on this guide)
3. **What actually happened** (observed behavior)
4. **SVG code snippet** (relevant section)
5. **Screenshots** (if visual issue)

This helps diagnose and fix problems quickly.

---

## Success Metrics

The skill is performing excellently if:

- ✅ 95%+ of slides generate correctly on first try
- ✅ 100% of slides are Figma-compatible
- ✅ 100% brand compliance
- ✅ <30 second average generation time
- ✅ <50 KB average file size
- ✅ User satisfaction (subjective but important!)

---

## Validation Complete?

Once you've run through these tests and everything passes, you can confidently use the SVG Slide Master for production work.

**The skill is designed for exceptional quality. These tests ensure it delivers on that promise.**

---

**Last validated:** [Add date when you run this validation]
**Validated by:** [Your name]
**Status:** [Pass/Fail/Needs Attention]
