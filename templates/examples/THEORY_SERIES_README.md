# Theoretical Framework Series - Methodology Overview

Professional 6-slide series explaining the theoretical basis for combining SHAP/Machine Learning with traditional statistical approaches (DLNM, random/mixed effects models) in climate-health research.

## Overview

This cohesive presentation series provides a rigorous theoretical foundation for your methodological approach in the HE²AT Centre Research Programme 2. Each slide is designed for academic audiences, ethics committee presentations, or PhD defense contexts.

**Target audience:** Research supervisors, ethics committees, methodological reviewers, PhD examiners

**Presentation time:** 18-25 minutes (3-4 minutes per slide)

---

## The 6 Slides

### 1. Title Slide
**File:** `theory-01-title.svg` | **Size:** 2.6 KB

**Content:**
- Main title: "Methodological Framework"
- Subtitle: "SHAP/Machine Learning vs Traditional Statistical Approaches"
- Context: "Theoretical Basis for Climate-Health Research"
- HE²AT Centre | Research Programme 2

**Use:** Opening slide for methodology presentations, introduces theoretical framework

---

### 2. SHAP / Shapley Values Foundation
**File:** `theory-02-shap-foundation.svg` | **Size:** 5.6 KB

**Content:**
- **Theoretical Origin:** Cooperative game theory roots
- **Shapley Formula:** φᵢ = Σ [ |S|!(n-|S|-1)! / n! ] × [ v(S ∪ {i}) - v(S) ]
- **Formal Properties:**
  - Local Accuracy (sum of attributions + baseline = output)
  - Consistency (marginal effect increase → SHAP value doesn't decrease)
  - Missingness (missing features get zero attribution)
- **In Machine Learning:**
  - Per-instance feature attribution
  - Model-agnostic (Kernel SHAP) or model-specific (TreeSHAP)
  - Handles non-linear, interactive models
  - Aggregates to global importance

**Key Insight Box:** "SHAP explains model behavior (prediction attribution), not necessarily causation. Ideal for feature screening in high-dimensional exposure spaces."

---

### 3. Traditional Statistical Approaches
**File:** `theory-03-traditional-methods.svg` | **Size:** 7.4 KB

**Content:** Two-column comparison

**DLNM (Left Column):**
- Distributed Lag Nonlinear Models
- Formula: log(μₜ) = α + Σ f(xₜ₋ₗ, ℓ) + ...
- Cross-basis function (exposure × lag)
- **Strengths:**
  - Explicit lag structure
  - Non-linear exposure-response curves
  - Established in climate-health literature
  - Policy-relevant effect estimates (RR, CI)
- Citations: Neophytou et al. 2018, Gasparrini et al. 2021

**Random/Mixed Effects (Right Column):**
- Hierarchical & spatial models
- Cluster-level variation (wards, regions)
- Random intercepts/slopes
- **Strengths:**
  - Within vs between-cluster variation
  - Formal inference with CIs
  - Handles confounding, effect modification
  - Interpretable for policymakers

**Application Note:** Spatial DLNMs combine both approaches (lag structure + random effects for region-specific curves)

---

### 4. Comparative Analysis
**File:** `theory-04-comparison.svg` | **Size:** 7.7 KB

**Content:** Side-by-side advantages/disadvantages

**SHAP / Machine Learning:**

✓ **Advantages:**
- High-dimensional feature spaces (many exposures, interactions)
- Instance-level interpretations (case-by-case variation)
- Model-agnostic flexibility (GBMs, RF, NNs)
- Efficient feature screening (50+ metrics)

✗ **Disadvantages:**
- Attribution ≠ Causation (explains predictions, not mechanisms)
- Correlated features issue (distorts rankings)
- Computational demands (expensive in large spaces)
- No inherent lag structure (unless built into features)

**DLNM / Random Effects:**

✓ **Advantages:**
- Designed for causal inference (formal effect estimates, lags, CIs)
- Temporal/spatial structure (handles correlation, clusters)
- Policy-relevant metrics (RR per unit, attributable fraction)
- Established in climate-health (strong precedence)

✗ **Disadvantages:**
- Limited high-dimensional capacity (not optimal for 50+ exposures)
- A priori specification required (basis functions, lag length)
- May miss complex interactions (unless specified)
- Computational intensity (spatial DLNM, Bayesian RE can be heavy)

**Citations:** Lundberg & Lee 2017, Molnar 2022, Kumar et al. 2020 (ML); Gasparrini 2011, Neophytou et al. 2018, Bhaskaran et al. 2013 (DLNM)

---

### 5. Proposed Integrated Workflow
**File:** `theory-05-integrated-workflow.svg` | **Size:** 7.9 KB

**Content:** 4-step process diagram with connecting arrows

**Step 1: ML + SHAP Screening**
- Build ML model (XGBoost) on all climate/socio-econ/land-use features
- **Output:** SHAP feature importance rankings

**Step 2: SHAP Inspection**
- Examine dependence plots
- Identify non-linearities, thresholds, interactions
- **Output:** Exposure patterns for model specification

**Step 3: DLNM/Random Effects Modelling**
- Specify models for top exposures with:
  - Lag structure
  - Spatial random effects
- **Output:** Effect estimates, lag curves, heterogeneity

**Step 4: Triangulation**
- Compare SHAP rankings with DLNM effect sizes
- Build heat-vulnerability index using both insights
- **Output:** Final interpretable model

**Key Benefit Box:** "Uses ML/SHAP breadth for discovery, DLNM/random effects depth for inference"

---

### 6. Key Cautions & Methodological Considerations
**File:** `theory-06-key-cautions.svg` | **Size:** 5.3 KB

**Content:** Warning icon (⚠️) with 5 critical considerations

**1. Feature Correlation & Multicollinearity**
- **Problem:** Climate exposures highly correlated (max temp, heat index, humidity, LST)
- **Mitigation:** Cluster correlated exposures (PCA/domain grouping); be explicit about ambiguity

**2. Temporal/Lag Structure**
- **Problem:** ML + SHAP doesn't inherently model lags unless features include them
- **Solution:** Include lagged features in ML input; use DLNM for explicit lag-response

**3. Causality vs Prediction**
- **Critical distinction:**
  - SHAP explains **model behavior** (prediction attribution)
  - DLNM estimates **causal associations** (with stated assumptions)

**4. Interpretability for Stakeholders**
- SHAP: Exploratory narrative
- DLNM: Dose-response curves for policy

**5. Computational Resources**
- ML + SHAP: Memory/compute intensive
- Spatial DLNM: Can be heavy but conceptually simpler

**References:** Kumar et al. 2020 (SHAP limitations), Bhaskaran et al. 2013 (DLNM autocorrelation), Molnar 2022 (Interpretable ML)

---

## Design Features

### Consistent Branding
All 6 slides feature:
- **Wits PHR identity** - Navy (#2c5cda), teal (#00bec5), blue (#20a3fc)
- **Inter font family** - Professional, academic typography
- **Clear hierarchy** - Titles (64px), headers (32-36px), body (20-24px)
- **Structured layouts** - Logical flow, generous whitespace

### Visual Elements
- **Color coding:**
  - Blue for SHAP/ML (innovation, technology)
  - Orange/gold for traditional methods (established, reliable)
  - Red for cautions/warnings
  - Teal/green for solutions/benefits
- **Gradient headers** - Professional polish
- **Highlight boxes** - Key insights stand out
- **Formula displays** - Academic credibility
- **Icons** - Warning symbol for cautions slide

### File Specifications
- **Format:** SVG (Scalable Vector Graphics)
- **Dimensions:** 1920×1080px (16:9)
- **Total series size:** 36.5 KB (all 6 slides)
- **Average per slide:** 6.1 KB
- **Figma-ready:** All text editable, layers organized

---

## Using This Series

### Complete Methodology Presentation

**Suggested sequence (20-25 minutes):**

1. **Title** (1 min) - Set context, introduce framework
2. **SHAP Foundation** (4-5 min) - Theoretical grounding, game theory
3. **Traditional Methods** (4-5 min) - DLNM and random effects overview
4. **Comparison** (5-6 min) - Discuss trade-offs, advantages/disadvantages
5. **Integrated Workflow** (4-5 min) - Show how to combine approaches
6. **Cautions** (3-4 min) - Acknowledge limitations, mitigation strategies

**Narrative arc:**
- Establish theoretical foundations (Slides 1-3)
- Compare approaches rigorously (Slide 4)
- Propose integration (Slide 5)
- Demonstrate methodological awareness (Slide 6)

---

### For Specific Contexts

**Ethics Committee Review:**
- Slides 1, 2, 3, 5, 6 (skip detailed comparison)
- Emphasize cautions slide (methodological awareness)
- Focus on workflow (how you'll actually do it)

**PhD Confirmation/Transfer:**
- All 6 slides (full theoretical depth)
- Extended discussion on Slide 4 (comparison)
- Show you understand trade-offs

**Research Group Presentation:**
- Slides 1, 5, 6 (skip detailed theory)
- Focus on workflow and practical considerations
- More time on how to implement

**Grant Proposal Defense:**
- Slides 1, 4, 5 (skip detailed foundations)
- Emphasize comparative advantage
- Show integration creates novel approach

---

## Theoretical Grounding

### Key Concepts Covered

1. **Game Theory Foundations** - Shapley value axioms, fair attribution
2. **Model Interpretability** - Local vs global explanations, SHAP properties
3. **Epidemiological Inference** - Lag-response, exposure-response surfaces
4. **Hierarchical Modelling** - Random effects, cluster variation
5. **Feature Screening** - High-dimensional reduction strategies
6. **Causal vs Predictive** - Critical methodological distinction

### Academic Rigor

Each slide includes:
- **Formal definitions** - Mathematical notation where appropriate
- **Key properties** - Theoretical guarantees (consistency, accuracy)
- **Established methods** - Precedence in literature
- **Methodological awareness** - Limitations and trade-offs
- **Citations** - Key references for each approach

---

## Customization Guide

### Easy Modifications

**Update institution/program:**
```svg
<text ...>HE²AT Centre | Research Programme 2</text>
<!-- Change to your program name -->
```

**Adjust formula notation:**
All formulas use plain text (not LaTeX) for SVG compatibility. Edit directly:
```svg
<text class="formula">φᵢ = Σ ...</text>
```

**Change color scheme:**
Gradients and colors defined in `<defs>`:
- `#2c5cda` (navy) → your primary color
- `#00bec5` (teal) → your secondary color

**Add/remove cautions:**
Slide 6 has 5 caution boxes - easy to add more or remove

---

## Integration with Other Materials

### Works Well With

**SHAP Examples Series (slides 01-05):**
- This theoretical framework + SHAP examples = complete package
- Use theory slides first, then show applications

**Your Research Presentations:**
- Insert relevant slides from this series into longer talks
- Slide 5 (workflow) particularly useful for methods sections

**Grant Proposals:**
- Export slides as high-res PNGs
- Include in methodology section as figures

---

## Quality Assurance

All slides verified for:

✅ **Academic credibility** - Proper citations, formal notation
✅ **Theoretical accuracy** - Formulas and properties correct
✅ **Balanced presentation** - Advantages AND disadvantages
✅ **Methodological awareness** - Acknowledges limitations
✅ **Visual clarity** - Clean layouts, readable at presentation size
✅ **Figma compatibility** - Text editable, layers organized
✅ **Brand compliance** - Wits PHR colors and standards
✅ **File optimization** - Small sizes, fast loading

---

## Technical Notes

### SVG Structure

All slides follow this pattern:
```xml
<svg viewBox="0 0 1920 1080">
  <defs>
    <!-- Styles, gradients, markers -->
  </defs>
  <g id="background">...</g>
  <g id="title">...</g>
  <g id="content">...</g>
  <g id="branding">...</g>
</svg>
```

### Typography Hierarchy

- **Slide titles:** 64px, bold, navy
- **Section headers:** 32-36px, bold, black or navy
- **Body text:** 20-24px, regular, dark gray
- **Captions/citations:** 16-18px, italic, gray

### Color Palette

**Primary:**
- Navy: #2c5cda
- Teal: #00bec5
- Blue: #20a3fc

**Accents:**
- Orange: #e67e22
- Gold: #d68910
- Red: #cc1a1b (warnings)

**Neutrals:**
- White: #ffffff
- Light gray: #f4f4f4
- Dark gray: #424242
- Black: #1a1a1a

---

## Key References Cited

### SHAP / Machine Learning
- Lundberg & Lee (2017) - Original SHAP paper
- Molnar (2022) - Interpretable Machine Learning book
- Kumar et al. (2020) - SHAP limitations and biases

### DLNM / Epidemiological Methods
- Gasparrini (2011) - Original DLNM methodology
- Neophytou et al. (2018) - DLNM application in cohorts
- Gasparrini et al. (2021) - DLNM extensions for cumulative effects
- Bhaskaran et al. (2013) - Time series regression for environmental studies

### Methodological Considerations
- Multiple papers on autocorrelation in time series
- Feature selection in high-dimensional spaces
- Causal inference in epidemiology

---

## Presentation Tips

### Timing

- **Don't rush theory** - Slides 2-3 need 4-5 min each
- **Emphasize comparison** - Slide 4 is crucial (5-6 min)
- **Workflow is key** - Slide 5 shows your actual plan (4-5 min)
- **End with awareness** - Slide 6 shows methodological maturity

### Delivery

- **Explain formulas** - Don't just read them, interpret
- **Use examples** - "In my dataset, temp and heat index correlate 0.95..."
- **Connect to research** - "This is why I'm using XGBoost for screening..."
- **Acknowledge critiques** - Show you've thought deeply about limitations

### Q&A Preparation

Likely questions:
- "Why not just use DLNM for everything?"
- "How do you handle correlated exposures?"
- "What if SHAP and DLNM disagree?"
- "Computational feasibility with your data size?"

Have answers ready (content in slides supports them all).

---

## Future Enhancements

Potential additions:
- **Slide 7:** Detailed case study example
- **Slide 8:** Simulation/validation approach
- **Slide 9:** Computational workflow diagram
- **Slide 10:** Timeline for implementation

Contact Wits PHR Data Science team for custom extensions.

---

## Summary

📊 **6 slides** covering complete theoretical framework
🎓 **Academic rigor** with proper citations and formal notation
⚖️ **Balanced analysis** of advantages and disadvantages
🔄 **Integrated approach** combining ML and traditional statistics
⚠️ **Methodological awareness** acknowledging limitations
✨ **Production-ready** for ethics, confirmation, defense presentations

**Total: 36.5 KB | ~20-25 minute presentation | Figma-editable**

---

**Created:** 2025-10-29
**For:** HE²AT Centre Research Programme 2, Wits PHR
**Purpose:** Theoretical basis for SHAP + DLNM integrated methodology
**Status:** Production-ready academic presentation

Use this series to establish your methodological framework with confidence and rigor! 🎯📐
