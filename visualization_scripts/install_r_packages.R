#!/usr/bin/env Rscript
################################################################################
# Install R Packages for DLNM Analysis
################################################################################

cat("Installing required R packages for DLNM analysis...\n\n")

# List of required packages
packages <- c(
  "dlnm",          # Distributed Lag Non-Linear Models
  "splines",       # Spline functions (usually pre-installed)
  "mgcv",          # GAM models (usually pre-installed)
  "ggplot2",       # Plotting
  "viridis",       # Color scales
  "RColorBrewer"   # Color palettes
)

# Install packages that aren't already installed
for (pkg in packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    cat(sprintf("Installing %s...\n", pkg))
    install.packages(pkg, repos = "https://cloud.r-project.org/")
  } else {
    cat(sprintf("✓ %s already installed\n", pkg))
  }
}

cat("\n✓ All required packages installed!\n")
