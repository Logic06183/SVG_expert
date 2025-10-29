#!/usr/bin/env python3
"""
SHAP Analysis for Climate-Biomarker Research
==============================================

Generates publication-quality SHAP visualizations showing:
1. Bee swarm plot (feature importance)
2. Dependence plots (non-linear relationships)

For CD4 count prediction using climate and socioeconomic variables.

Author: Wits Planetary Health Research
Date: 2025-10-29
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import shap

# Set random seed for reproducibility
np.random.seed(42)

# Set publication-quality plotting defaults
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

def generate_climate_biomarker_data(n_samples=5000):
    """
    Generate synthetic climate-biomarker dataset with realistic relationships.

    Features:
    - Climate: Max temp, mean temp, humidity, heat index
    - Demographics: Age, sex
    - Socioeconomic: Education level, income

    Outcome: CD4 count (cells/μL)

    Returns:
    - X: Feature dataframe
    - y: CD4 counts
    """

    # Climate variables
    max_temp = np.random.normal(25, 5, n_samples)  # °C, mean 25°C
    mean_temp = max_temp - np.random.uniform(3, 7, n_samples)  # °C
    humidity = np.random.uniform(40, 80, n_samples)  # %
    heat_index = max_temp + 0.3 * humidity + np.random.normal(0, 2, n_samples)

    # Demographics
    age = np.random.gamma(4, 10, n_samples) + 18  # Age distribution skewed towards younger
    age = np.clip(age, 18, 75)
    sex = np.random.binomial(1, 0.52, n_samples)  # 52% female

    # Socioeconomic
    education = np.random.choice([1, 2, 3, 4, 5], n_samples,
                                 p=[0.15, 0.25, 0.30, 0.20, 0.10])  # 1=primary, 5=tertiary
    income = np.random.lognormal(9, 0.7, n_samples)  # ZAR/month, log-normal distribution
    income = np.clip(income, 1000, 50000)

    # Generate CD4 count with realistic relationships
    cd4_base = 500  # baseline CD4

    # Temperature effect (J-shaped: optimal around 22°C)
    temp_effect = -0.3 * (max_temp - 22)**2

    # Extreme heat effect (threshold at 30°C)
    extreme_heat = np.where(max_temp > 30, -15 * (max_temp - 30), 0)

    # Humidity effect (slight negative)
    humidity_effect = -0.5 * (humidity - 60)

    # Age effect (decline with age)
    age_effect = -2 * (age - 35)

    # Sex effect (slightly lower in males)
    sex_effect = -30 * (1 - sex)

    # Education effect (positive, saturating)
    education_effect = 40 * np.log(education + 1)

    # Income effect (positive, logarithmic)
    income_effect = 30 * np.log(income / 5000)

    # Combine effects with noise
    cd4 = (cd4_base +
           temp_effect + extreme_heat +
           humidity_effect +
           age_effect + sex_effect +
           education_effect + income_effect +
           np.random.normal(0, 50, n_samples))

    # Clip to realistic CD4 range
    cd4 = np.clip(cd4, 50, 1200)

    # Create dataframe
    X = pd.DataFrame({
        'Max Temperature (°C)': max_temp,
        'Mean Temperature (°C)': mean_temp,
        'Humidity (%)': humidity,
        'Heat Index': heat_index,
        'Age (years)': age,
        'Sex (Female=1)': sex,
        'Education Level': education,
        'Income (ZAR/month)': income
    })

    return X, cd4

def train_model(X, y):
    """Train gradient boosting model."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = GradientBoostingRegressor(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    print(f"Model Performance:")
    print(f"  Training R²: {train_score:.3f}")
    print(f"  Testing R²: {test_score:.3f}")

    return model, X_train, X_test, y_train, y_test

def create_shap_bee_swarm(model, X, output_path='outputs/shap_beeswarm.png'):
    """Create SHAP bee swarm plot showing feature importance."""

    # Calculate SHAP values
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    # Create bee swarm plot
    fig, ax = plt.subplots(figsize=(10, 6))
    shap.summary_plot(shap_values, X, show=False, plot_size=(10, 6))

    plt.xlabel('SHAP value (impact on CD4 count, cells/μL)', fontsize=12, fontweight='bold')
    plt.title('Feature Importance for CD4 Count Prediction\nBee Swarm Plot',
              fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Saved bee swarm plot to {output_path}")
    plt.close()

    return shap_values, explainer

def create_shap_dependence_plots(shap_values, X, output_path='outputs/shap_dependence.png'):
    """Create SHAP dependence plots for key features."""

    # Select key features to plot
    features_to_plot = [
        'Max Temperature (°C)',
        'Income (ZAR/month)',
        'Age (years)',
        'Humidity (%)'
    ]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    for idx, feature in enumerate(features_to_plot):
        plt.sca(axes[idx])
        shap.dependence_plot(
            feature,
            shap_values,
            X,
            show=False,
            ax=axes[idx]
        )
        axes[idx].set_title(f'SHAP Dependence: {feature}',
                           fontsize=12, fontweight='bold')
        axes[idx].set_xlabel(feature, fontsize=11)
        axes[idx].set_ylabel('SHAP value\n(impact on CD4)', fontsize=11)

        # Add zero line
        axes[idx].axhline(y=0, color='gray', linestyle='--',
                         linewidth=1, alpha=0.5)

    plt.suptitle('Non-Linear Relationships: SHAP Dependence Plots',
                 fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Saved dependence plots to {output_path}")
    plt.close()

def create_summary_statistics(X, y, shap_values):
    """Print summary statistics and feature importance."""

    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)

    print(f"\nDataset: N = {len(X):,} observations")
    print(f"CD4 count range: {y.min():.0f} - {y.max():.0f} cells/μL")
    print(f"CD4 count mean: {y.mean():.0f} (SD: {y.std():.0f})")

    print("\nFeature Statistics:")
    print(X.describe().round(2))

    print("\nFeature Importance (mean |SHAP value|):")
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Mean |SHAP|': np.abs(shap_values).mean(axis=0)
    }).sort_values('Mean |SHAP|', ascending=False)

    for idx, row in feature_importance.iterrows():
        print(f"  {row['Feature']:<30} {row['Mean |SHAP|']:.3f}")

def main():
    """Main execution function."""

    print("="*60)
    print("SHAP ANALYSIS: Climate-Biomarker Research")
    print("="*60)
    print()

    # Create output directory
    import os
    os.makedirs('outputs', exist_ok=True)

    # Generate data
    print("Generating synthetic climate-biomarker data...")
    X, y = generate_climate_biomarker_data(n_samples=5000)
    print(f"✓ Generated {len(X):,} observations")

    # Train model
    print("\nTraining gradient boosting model...")
    model, X_train, X_test, y_train, y_test = train_model(X, y)

    # Create SHAP visualizations
    print("\nGenerating SHAP visualizations...")
    shap_values, explainer = create_shap_bee_swarm(model, X_test)
    create_shap_dependence_plots(shap_values, X_test)

    # Summary statistics
    create_summary_statistics(X_test, y_test, shap_values)

    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print("\nOutputs saved to:")
    print("  - outputs/shap_beeswarm.png")
    print("  - outputs/shap_dependence.png")
    print()

if __name__ == '__main__':
    main()
