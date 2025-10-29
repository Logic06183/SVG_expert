#!/bin/bash
################################################################################
# Run All Visualization Scripts
################################################################################
#
# This script runs both SHAP (Python) and DLNM (R) analyses and generates
# all publication-quality visualizations.
#
# Usage: bash run_all.sh
#
################################################################################

set -e  # Exit on error

echo "========================================================================"
echo "Climate-Biomarker Visualization Pipeline"
echo "========================================================================"
echo ""

# Create outputs directory
mkdir -p outputs

# Run Python SHAP analysis
echo "Step 1: Running SHAP analysis (Python)..."
echo "------------------------------------------------------------------------"
python3 01_shap_analysis.py
echo ""

# Run R DLNM analysis
echo "Step 2: Running DLNM analysis (R)..."
echo "------------------------------------------------------------------------"
Rscript 02_dlnm_analysis.R
echo ""

# Summary
echo "========================================================================"
echo "ALL ANALYSES COMPLETE"
echo "========================================================================"
echo ""
echo "Generated visualizations:"
echo ""
echo "SHAP Analysis (Python):"
echo "  ✓ outputs/shap_beeswarm.png"
echo "  ✓ outputs/shap_dependence.png"
echo ""
echo "DLNM Analysis (R):"
echo "  ✓ outputs/dlnm_surface_3d.png"
echo "  ✓ outputs/dlnm_contour.png"
echo "  ✓ outputs/dlnm_lag_curves.png"
echo "  ✓ outputs/dlnm_overall_curve.png"
echo ""
echo "All plots are high-resolution (300 DPI) and ready for publication!"
echo ""
