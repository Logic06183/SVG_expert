# Climate-Biomarker Visualization Scripts

**Production-ready Python and R scripts for generating authentic SHAP and DLNM visualizations**

This directory contains scripts that generate publication-quality visualizations using native Python (`shap`) and R (`dlnm`) packages, showing realistic climate-biomarker relationships for CD4 count prediction.

---

## 📁 Contents

```
visualization_scripts/
├── 01_shap_analysis.py          # Python: SHAP bee swarm + dependence plots
├── 02_dlnm_analysis.R           # R: DLNM lag-response surfaces and curves
├── requirements.txt             # Python package dependencies
├── install_r_packages.R         # R package installation script
├── README.md                    # This file
└── outputs/                     # Generated plots saved here
```

---

## 🎯 What These Scripts Do

### 1. SHAP Analysis (Python)

**File:** `01_shap_analysis.py`

**Generates:**
- **Bee swarm plot** - Feature importance with colored dots showing feature values
- **Dependence plots** (4 panels) - Non-linear relationships for key features
  - Maximum Temperature (J-shaped curve)
  - Income (logarithmic saturation)
  - Age (linear decline)
  - Humidity (slight negative)

**Features modeled:**
- Climate: Max temperature, mean temperature, humidity, heat index
- Demographics: Age, sex
- Socioeconomic: Education level, income

**Output:** CD4 count (cells/μL)

---

### 2. DLNM Analysis (R)

**File:** `02_dlnm_analysis.R`

**Generates:**
- **3D lag-response surface** - Temperature × Lag interaction (perspective plot)
- **Contour plot** - 2D heatmap of lag-response surface
- **Lag-specific curves** - Temperature-response at lags 0, 3, 7, 14 days
- **Overall cumulative curve** - Total effect over 0-14 days

**Model specification:**
- Natural cubic splines for temperature (df=4) and lag (df=3)
- Reference temperature: 22°C
- Lag structure: 0-14 days
- Adjusted for: humidity, age, sex, education, income, seasonality, long-term trend

**Output:** CD4 count effect estimates

---

## 🚀 Quick Start

### Prerequisites

**Python:** Version 3.8+ with pip
**R:** Version 4.0+ with package installation capability

### Installation

#### Python Packages

```bash
cd visualization_scripts
pip install -r requirements.txt
```

This installs:
- `numpy`, `pandas` - Data manipulation
- `matplotlib`, `seaborn` - Plotting
- `scikit-learn` - Machine learning models
- `shap` - SHAP value computation

#### R Packages

```bash
Rscript install_r_packages.R
```

This installs:
- `dlnm` - Distributed lag non-linear models
- `mgcv` - Generalized additive models
- `ggplot2`, `viridis`, `RColorBrewer` - Visualization

---

## 📊 Running the Analyses

### SHAP Analysis

```bash
python 01_shap_analysis.py
```

**Output files:**
- `outputs/shap_beeswarm.png` - Feature importance bee swarm plot
- `outputs/shap_dependence.png` - 4-panel dependence plots

**Runtime:** ~30 seconds
**Dataset:** 5,000 synthetic observations

---

### DLNM Analysis

```bash
Rscript 02_dlnm_analysis.R
```

**Output files:**
- `outputs/dlnm_surface_3d.png` - 3D perspective plot
- `outputs/dlnm_contour.png` - 2D heatmap
- `outputs/dlnm_lag_curves.png` - Lag-specific curves
- `outputs/dlnm_overall_curve.png` - Cumulative curve

**Runtime:** ~1-2 minutes
**Dataset:** 2,000 days (5.5 years) of synthetic daily observations

---

## 🎨 Visualization Details

### SHAP Bee Swarm Plot

**What it shows:**
- Y-axis: Features ranked by importance
- X-axis: SHAP values (impact on CD4 count)
- Color: Feature value (blue = low, red = high)
- Each dot = one observation

**Interpretation:**
- Features spread wide = high impact
- Red dots to the right = high feature value increases CD4
- Blue dots to the left = low feature value decreases CD4

**Realistic patterns:**
- Income, education: Strong positive effects
- Max temperature: J-shaped (moderate optimal, extreme negative)
- Age: Negative effect (older = lower CD4)

---

### SHAP Dependence Plots

**What they show:**
- X-axis: Feature value
- Y-axis: SHAP value (marginal effect on CD4)
- Color: Interaction with other features
- Smoothed trend line shows non-linearity

**Key patterns:**
- **Temperature:** J-shaped curve, optimal ~22°C, sharp decline >30°C
- **Income:** Logarithmic saturation, plateaus at high income
- **Age:** Linear negative relationship
- **Humidity:** Slight negative effect, relatively flat

---

### DLNM 3D Surface

**What it shows:**
- X-axis: Temperature (°C)
- Y-axis: Lag (days 0-14)
- Z-axis: Relative effect on CD4
- Color: Effect magnitude (blue = protective, red = harmful)

**Interpretation:**
- Immediate effect (lag 0): Strong at extreme temps
- Peak lag: Usually 3-5 days for temperature
- Cumulative pattern visible across lag dimension

---

### DLNM Overall Curve

**What it shows:**
- X-axis: Temperature (°C)
- Y-axis: Cumulative effect on CD4 (sum of all lags)
- Shaded area: 95% confidence interval
- Reference line at 22°C (centered)

**Interpretation:**
- U-shaped or J-shaped curve expected
- Effects quantified as CD4 cells/μL change
- Confidence intervals show statistical uncertainty

---

## 🔬 Synthetic Data Generation

Both scripts generate realistic synthetic data with known relationships:

### Relationships Modeled

**Temperature effects:**
- J-shaped: Optimal around 22°C
- Negative quadratic: -0.3 × (temp - 22)²
- Threshold effect: Strong negative above 30°C
- Lagged effects: Decay over 1-3 days

**Socioeconomic effects:**
- Income: Logarithmic (diminishing returns)
- Education: Positive, categorical (1-5 levels)
- Age: Linear negative (-2 cells/μL per year from age 35)
- Sex: Slight difference (females +30 cells/μL)

**Noise:**
- Random variation: N(0, 40-50)
- Seasonality: Sinusoidal annual cycle
- Long-term trends: Linear time effect

---

## 📐 Model Specifications

### SHAP Model

**Algorithm:** Gradient Boosting Regressor
**Parameters:**
- n_estimators: 100
- max_depth: 4
- learning_rate: 0.1

**SHAP method:** TreeExplainer (exact for tree models)

**Expected performance:** R² ≈ 0.75-0.80 on test set

---

### DLNM Model

**Base model:** Generalized Additive Model (GAM)

**Cross-basis specification:**
- Temperature: Natural cubic spline, df=4
- Lag: Natural cubic spline, df=3
- Lag range: 0-14 days

**Confounders:**
- Humidity: Smooth term, k=4
- Age: Smooth term, k=4
- Sex: Linear term
- Education: Smooth term, k=4
- Log(income): Smooth term, k=4
- Time trend: Smooth term, k=10
- Seasonality: Cyclic cubic spline, k=12

**Reference:** 22°C (comfortable temperature)

**Expected performance:** Deviance explained ≈ 60-70%

---

## 📝 Customization

### Modify Variables

**Python (SHAP):**
Edit `generate_climate_biomarker_data()` function:
```python
# Add new feature
new_feature = np.random.normal(0, 1, n_samples)
X['New Feature'] = new_feature

# Add to CD4 generation
new_effect = 10 * new_feature
cd4 = cd4_base + ... + new_effect + ...
```

**R (DLNM):**
Edit `generate_climate_biomarker_timeseries()` function:
```r
# Add new exposure
new_exposure <- rnorm(n_days, 0, 1)

# Add to model formula
model <- gam(cd4 ~ cb_temp + s(new_exposure, k=4) + ...)
```

---

### Change Sample Size

**Python:**
```python
X, y = generate_climate_biomarker_data(n_samples=10000)  # Default: 5000
```

**R:**
```r
data <- generate_climate_biomarker_timeseries(n_days=3650)  # Default: 2000
```

---

### Adjust Lag Structure

**R DLNM:**
```r
cb_temp <- crossbasis(
  data$max_temp,
  lag = 21,  # Change from 14 to 21 days
  argvar = list(fun = "ns", df = 4),
  arglag = list(fun = "ns", df = 4)  # Increase complexity
)
```

---

### Change Plot Aesthetics

**Python:**
Edit plotting parameters:
```python
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 12
shap.summary_plot(..., plot_size=(12, 8))  # Larger plot
```

**R:**
Edit plot parameters:
```r
png(output_path, width = 4000, height = 3000, res = 300)  # Higher res
plot(..., col = brewer.pal(11, "Spectral"))  # Different colors
```

---

## 🎓 Educational Use

These scripts are ideal for:
- **Teaching** - Show students how SHAP and DLNM work with real code
- **Presentations** - Generate publication-quality figures
- **Proposals** - Demonstrate methodological approach
- **Thesis** - Include as methods appendix with adaptations

### Learning Objectives

**SHAP:**
- Understand feature importance vs. feature effect
- Recognize non-linear patterns in dependence plots
- Interpret interaction effects (color in dependence plots)

**DLNM:**
- Understand lag-response relationships
- Interpret 3D surfaces and contours
- Distinguish immediate vs. cumulative effects
- Recognize U-shaped or J-shaped exposure-response curves

---

## 📚 References

### SHAP

- Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *NIPS 2017*. [arXiv:1705.07874](https://arxiv.org/abs/1705.07874)
- SHAP GitHub: https://github.com/slundberg/shap

### DLNM

- Gasparrini, A. (2011). Distributed lag non-linear models. *Statistics in Medicine*, 30(21), 2631-2647.
- Gasparrini, A., Armstrong, B., & Kenward, M. G. (2010). Distributed lag non-linear models. *Biostatistics*, 11(3), 532-543.
- DLNM R package: https://cran.r-project.org/package=dlnm

---

## 🐛 Troubleshooting

### Python Issues

**ImportError: No module named 'shap'**
```bash
pip install --upgrade shap
```

**Matplotlib backend errors:**
```python
# Add at top of script
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
```

---

### R Issues

**Package installation fails:**
```r
# Try different repository
install.packages("dlnm", repos = "https://cran.rstudio.com/")

# Or install dependencies first
install.packages(c("splines", "mgcv"))
```

**Graphics device errors:**
```r
# Make sure to close devices
dev.off()

# Or specify device explicitly
png(..., type = "cairo")
```

---

## 💡 Tips for Best Results

### SHAP Analysis

✅ **DO:**
- Use at least 1,000 observations for stable SHAP values
- Check model performance (R² > 0.7) before interpreting
- Look for consistent patterns across multiple features
- Use dependence plots to understand HOW features work

❌ **DON'T:**
- Over-interpret small SHAP values (focus on top features)
- Assume SHAP = causality (it shows associations)
- Ignore interaction effects (shown by color variation)

---

### DLNM Analysis

✅ **DO:**
- Use time series data (daily/weekly observations)
- Include sufficient lag period (14-21 days for temperature)
- Adjust for seasonality and long-term trends
- Center at a meaningful reference value
- Check confidence intervals (wide = uncertain)

❌ **DON'T:**
- Use with cross-sectional data (need temporal structure)
- Ignore confounders (biased effect estimates)
- Over-extrapolate beyond observed temperature range
- Forget to account for delayed effects in interpretation

---

## 📧 Contact

**Questions or issues?**

- Wits Planetary Health Research Data Science Team
- HE²AT Centre Research Programme 2

**For custom analysis or adaptations:**
Contact the research team for consultation on applying these methods to your specific climate-health research question.

---

## 📄 License

These scripts are provided for educational and research purposes.
Adapt freely for your own climate-health biomarker research.

---

**Created:** 2025-10-29
**Version:** 1.0
**Status:** Production-ready

Generate beautiful, authentic climate-health visualizations with confidence! 🎯📊🌡️
