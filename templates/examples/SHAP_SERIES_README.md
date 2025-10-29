# SHAP Research Overview Slides - Presentation Series

Professional slide series showcasing SHAP (SHapley Additive exPlanations) applications across health and exposure science domains. Created for Wits Planetary Health Research presentations.

## Overview

This is a cohesive 5-slide series that demonstrates the breadth and applicability of SHAP values in various health research contexts. Each slide follows a consistent format:

- **Title** - Study domain and focus
- **Key Findings** (left column) - Study design, methods, SHAP results
- **Relevance to Your Work** (right column) - How it applies to climate-health research
- **Citation** (footer) - Full reference for the study
- **Wits PHR Branding** - Consistent visual identity

## The 5 Slides

### 1. Lifestyle Factors & Obesity (2024)
**File:** `shap-01-lifestyle-obesity.svg` | **Size:** 8.5 KB

**Study Focus:**
- Pooled data: ~46,000 adults (China & USA)
- Algorithm: Gradient Boosting Decision Tree
- Top predictors: Sedentary behavior, alcohol, protein intake
- Actionable thresholds identified

**Key Relevance:**
- Multi-exposure screening methodology
- Demonstrates feature selection before deep modeling
- Cross-population validation approach

**Citation:** BMC Public Health, 2024

---

### 2. Social Determinants & Post-Stroke Depression (2025)
**File:** `shap-02-social-depression.svg` | **Size:** 8.4 KB

**Study Focus:**
- Sample: ~70,000 NHANES participants
- Outcome: Post-stroke depression (PSD)
- Algorithm: CatBoost (AUC = 0.966)
- SHAP revealed social determinants (income, education, food security) as strong predictors

**Key Relevance:**
- Integrating socio-economic with clinical data
- Multi-dimensional risk factor modeling
- Large-scale population data analysis

**Citation:** BMC Public Health, 2025

---

### 3. Heavy Metals & Chronic Bronchitis (2025)
**File:** `shap-03-heavy-metals-bronchitis.svg` | **Size:** 8.6 KB

**Study Focus:**
- Sample: 7,493 participants (US nationally representative)
- Exposures: Blood/urine heavy metals (Cd, Pb)
- Algorithm: CatBoost
- Top contributor: Blood-cadmium concentration

**Key Relevance:**
- Environmental exposome parallel to climate exposures
- Non-linear detection before DLNM modeling
- Feature screening from high-dimensional data

**Citation:** BMC Pulmonary Medicine, 2025

---

### 4. Postpartum Hemorrhage Prediction (2025)
**File:** `shap-04-postpartum-hemorrhage.svg` | **Size:** 8.6 KB

**Study Focus:**
- Retrospective cohort: Women with vaginal births
- Outcome: Postpartum hemorrhage (PPH)
- ML + SHAP for prediction and interpretation
- Clinically interpretable risk assessment

**Key Relevance:**
- Methodological precedent for birth outcomes
- Direct relevance to preterm birth research
- Interpretability for clinical stakeholders

**Citation:** BMC Pregnancy and Childbirth, 2025

---

### 5. Heavy Metals & Alveolar Bone Loss (2025)
**File:** `shap-05-heavy-metals-bone-loss.svg` | **Size:** 8.6 KB

**Study Focus:**
- Data: NHANES 2015-2018
- Outcome: Alveolar bone loss (dental health)
- Top metals: Cadmium (strongest), cobalt, lead
- Income identified as effect modifier

**Key Relevance:**
- High-dimensional exposure analysis
- Effect modification detection (socio-economic factors)
- Bee-swarm plot visualization techniques

**Citation:** BMC Public Health, 2025

---

## Design Features

### Consistent Layout
All 5 slides share:
- **Two-column structure** - Key Findings (left) vs Relevance (right)
- **Color-coded headers** - Blue-teal gradient (findings), orange-gold gradient (relevance)
- **Wits PHR branding** - Navy (#2c5cda), teal (#00bec5), blue (#20a3fc), orange (#e67e22)
- **Professional typography** - Inter font family, clear hierarchy
- **Citation footer** - Full references in gray box

### Visual Elements
- **Bullet points** - Color-coded circles (navy for standard, red/gold/blue for importance ranking)
- **Highlight boxes** - Light blue (#e3ecfc) for SHAP results, cream (#fde4cd) for applications
- **Application boxes** - "💡 Your Pipeline Application" sections in all slides
- **Consistent spacing** - 100px margins, generous whitespace

### File Specifications
- **Format:** SVG (Scalable Vector Graphics)
- **Dimensions:** 1920×1080px (16:9)
- **Average file size:** 8.5 KB per slide
- **Total series size:** 42.7 KB (all 5 slides)
- **Figma-ready:** All text editable, layers organized

## Using This Series

### As a Complete Presentation Sequence

**Suggested Order:**

1. **Slide 1 (Lifestyle)** - Introduction to SHAP, feature screening
2. **Slide 2 (Social)** - Multi-dimensional exposures, SDoH integration
3. **Slide 3 (Heavy Metals)** - Environmental exposome, non-linearity
4. **Slide 4 (PPH)** - Birth outcomes, clinical relevance
5. **Slide 5 (Bone Loss)** - Effect modification, socio-economic interactions

**Narrative Arc:**
- Start with feature screening (Slide 1)
- Progress to multi-dimensional data (Slide 2)
- Show environmental parallel (Slide 3)
- Connect to birth outcomes (Slide 4)
- End with effect modification (Slide 5)

**Total presentation time:** ~15-20 minutes (3-4 min per slide)

---

### As Individual Reference Slides

Each slide stands alone and can be used independently:

- **Literature review presentations** - Cite specific studies
- **Methods sections** - Show precedent for SHAP in your domain
- **Grant proposals** - Demonstrate established methodology
- **Team meetings** - Discuss specific applications

---

### For Teaching/Training

Use the series to teach:
- **SHAP methodology** - Multiple applications across domains
- **Feature importance** - Ranking predictors in complex models
- **Effect modification** - Socio-economic interactions
- **Model interpretation** - Making black-box models transparent

---

## Thematic Connections

### Environmental Exposome
- **Slide 1:** Lifestyle exposures
- **Slide 3:** Heavy metal exposures
- **Slide 5:** Heavy metal + income interactions

### Health Outcomes
- **Slide 2:** Post-stroke depression
- **Slide 4:** Postpartum hemorrhage
- **Slide 5:** Alveolar bone loss

### Socio-Economic Integration
- **Slide 2:** Social determinants as predictors
- **Slide 5:** Income as effect modifier

### Large-Scale Data
- **Slide 1:** 46,000 participants (CHNS + NHANES)
- **Slide 2:** 70,000 participants (NHANES)
- **Slide 3:** 7,493 participants (nationally representative)

---

## Relevance to Climate-Health Research

All 5 slides connect to your research pipeline:

### Your Research Program Components
1. **Climate exposures** → Heavy metal exposures (analogous)
2. **Land-use variables** → Lifestyle factors (multi-dimensional)
3. **Socio-economic data** → Income, education, housing (integrated)
4. **Birth outcomes** → Preterm birth, PPH (similar domain)
5. **Effect modification** → Income × climate interactions

### Pipeline Applications

**From each slide:**

1. **Lifestyle/Obesity** → Feature screening for 50+ climate metrics
2. **Social/Depression** → Integrate SDoH with climate exposures
3. **Heavy Metals/Bronchitis** → Non-linearity detection before DLNM
4. **PPH** → Birth outcome prediction with interpretability
5. **Bone Loss** → Identify which SDoH factors modify climate effects

---

## Customization Guide

### Easy Modifications

**Change titles:**
```svg
<text x="960" y="90" class="slide-title" text-anchor="middle">
  Your New Title Here
</text>
```

**Update bullets:**
```svg
<text x="155" y="300" class="body-text">
  <tspan x="155" dy="0">Your new bullet point text</tspan>
</text>
```

**Modify colors:**
All colors use named gradients and classes:
- `url(#header-left)` - Blue-teal gradient
- `url(#header-right)` - Orange-gold gradient
- Color classes: `.wits-navy`, `.accent-orange`, etc.

**Change citations:**
```svg
<text x="120" y="950" class="citation">
  Your new citation text
</text>
```

### Import to Figma

1. **File → Import** in Figma
2. Select SVG file(s)
3. All text remains editable
4. Layers organized by section

### Export Options

From Figma:
- **PNG** - For presentations (2x resolution recommended)
- **PDF** - For printing or document embedding
- **SVG** - Keep editable for future modifications

---

## Quality Assurance

All slides verified for:

✅ **Figma compatibility** - Text as `<text>` elements, not paths
✅ **Brand compliance** - Wits PHR colors and fonts
✅ **Typography** - Inter font, proper hierarchy
✅ **Accessibility** - WCAG AA color contrast
✅ **File size** - Optimized (<10 KB each)
✅ **Layout** - Consistent structure across series
✅ **Citations** - Accurate and complete

---

## Technical Specifications

### SVG Structure
```xml
<svg viewBox="0 0 1920 1080">
  <defs>
    <!-- Styles, gradients -->
  </defs>
  <g id="background">...</g>
  <g id="title">...</g>
  <g id="left-column">...</g>
  <g id="right-column">...</g>
  <g id="citation">...</g>
  <g id="branding">...</g>
</svg>
```

### Color Palette
- **Primary:** #2c5cda (navy), #00bec5 (teal), #20a3fc (blue)
- **Accent:** #e67e22 (orange), #d68910 (gold), #cc1a1b (red)
- **Neutrals:** #ffffff (white), #f4f4f4 (light gray), #424242 (dark gray)

### Typography
- **Font:** Inter (Google Fonts)
- **Weights:** 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
- **Sizes:** 48px (title), 32px (headers), 20px (body), 16px (citations)

---

## Additional Resources

### Related Examples in This Directory
- `shap-environmental-health-full.svg` - Comprehensive detailed slide
- `shap-key-finding.svg` - Impact statistic slide
- `shap-feature-ranking.svg` - Bar chart visualization
- `shap-methodology-flow.svg` - 4-step process diagram

### Documentation
- `README.md` - Main examples documentation
- `../README.md` - Template overview
- `../../README.md` - Repository guide

### Source References
All studies are 2024-2025 publications in BMC journals:
- BMC Public Health
- BMC Pulmonary Medicine
- BMC Pregnancy and Childbirth

---

## Future Additions

Potential slides to add to this series:
- Air pollution + respiratory outcomes
- Temperature extremes + cardiovascular health
- Climate variability + infectious disease
- Land use change + vector-borne disease
- Green space + mental health outcomes

Contact Wits PHR Data Science team for additional examples or custom slides.

---

## Summary

📊 **5 professional slides** covering diverse SHAP applications
🎨 **Consistent Wits PHR branding** throughout
📖 **Complete citations** for all studies
🔗 **Direct relevance** to climate-health research
✨ **Production-ready** for presentations
✏️ **Fully editable** in Figma

**Total series: 42.7 KB | Ready to present immediately**

---

**Created:** 2025-10-29
**For:** Wits Planetary Health Research
**Purpose:** Overview of SHAP methodology across health domains
**Status:** Production-ready presentation series

Use these slides to demonstrate the breadth of SHAP applications and build confidence in your methodological approach! 🌍
