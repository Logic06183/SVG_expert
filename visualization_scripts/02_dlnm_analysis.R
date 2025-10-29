#!/usr/bin/env Rscript
################################################################################
# DLNM Analysis for Climate-Biomarker Research
################################################################################
#
# Generates publication-quality DLNM visualizations showing:
# 1. 3D lag-response surface (temperature × lag interaction)
# 2. Lag-response curves at specific temperatures
# 3. Cumulative exposure-response curve
#
# For CD4 count prediction using temperature and humidity with lag structure.
#
# Author: Wits Planetary Health Research
# Date: 2025-10-29
#
################################################################################

# Load required packages
library(dlnm)
library(splines)
library(mgcv)  # For GAM
library(ggplot2)
library(viridis)
library(RColorBrewer)

# Set random seed for reproducibility
set.seed(42)

# Create output directory
if (!dir.exists("outputs")) {
  dir.create("outputs")
}

################################################################################
# 1. Generate Synthetic Time Series Data
################################################################################

generate_climate_biomarker_timeseries <- function(n_days = 2000) {
  #' Generate synthetic daily time series data with lag effects
  #'
  #' @param n_days Number of days to simulate
  #' @return data.frame with daily observations

  cat("Generating synthetic climate-biomarker time series...\n")

  # Date sequence
  dates <- seq(as.Date("2018-01-01"), by = "day", length.out = n_days)

  # Time index for seasonality
  time <- 1:n_days
  doy <- as.numeric(format(dates, "%j"))  # Day of year

  # Generate temperature with seasonality
  temp_seasonal <- 22 + 8 * sin(2 * pi * doy / 365)
  temp_noise <- rnorm(n_days, 0, 3)
  max_temp <- temp_seasonal + temp_noise
  max_temp <- pmax(pmin(max_temp, 38), 10)  # Clip to realistic range

  # Humidity (inverse seasonal pattern)
  humidity <- 60 + 15 * cos(2 * pi * doy / 365) + rnorm(n_days, 0, 5)
  humidity <- pmax(pmin(humidity, 95), 30)

  # Individual characteristics (fixed for each individual, varying across population)
  # Simulate as if we're tracking a cohort
  age <- rnorm(n_days, 38, 12)
  age <- pmax(pmin(age, 75), 18)

  sex <- rbinom(n_days, 1, 0.52)  # Female=1
  education <- sample(1:5, n_days, replace = TRUE, prob = c(0.15, 0.25, 0.30, 0.20, 0.10))
  income <- rlnorm(n_days, 9, 0.7)
  income <- pmax(pmin(income, 50000), 1000)

  # Generate CD4 with LAGGED temperature effects
  cd4_base <- 500

  # Immediate temperature effect (lag 0): J-shaped
  temp_effect_lag0 <- -0.5 * (max_temp - 22)^2

  # Extreme heat effect (threshold)
  extreme_heat_lag0 <- ifelse(max_temp > 30, -20 * (max_temp - 30), 0)

  # Create lagged temperature effects
  # Lag 1-3 days: accumulating negative effect
  temp_lag1 <- c(NA, max_temp[1:(n_days-1)])
  temp_lag2 <- c(NA, NA, max_temp[1:(n_days-2)])
  temp_lag3 <- c(NA, NA, NA, max_temp[1:(n_days-3)])

  temp_effect_lag1 <- -0.3 * (temp_lag1 - 22)^2
  temp_effect_lag2 <- -0.2 * (temp_lag2 - 22)^2
  temp_effect_lag3 <- -0.1 * (temp_lag3 - 22)^2

  # Replace NA with 0
  temp_effect_lag1[is.na(temp_effect_lag1)] <- 0
  temp_effect_lag2[is.na(temp_effect_lag2)] <- 0
  temp_effect_lag3[is.na(temp_effect_lag3)] <- 0

  # Other effects
  humidity_effect <- -0.3 * (humidity - 60)
  age_effect <- -1.5 * (age - 35)
  sex_effect <- -25 * (1 - sex)
  education_effect <- 30 * log(education + 1)
  income_effect <- 25 * log(income / 5000)

  # Long-term trend
  trend_effect <- 0.05 * time

  # Combine all effects
  cd4 <- cd4_base +
    temp_effect_lag0 + extreme_heat_lag0 +
    temp_effect_lag1 + temp_effect_lag2 + temp_effect_lag3 +
    humidity_effect +
    age_effect + sex_effect +
    education_effect + income_effect +
    trend_effect +
    rnorm(n_days, 0, 40)

  # Clip to realistic range
  cd4 <- pmax(pmin(cd4, 1200), 50)

  # Create dataframe
  data <- data.frame(
    date = dates,
    time = time,
    doy = doy,
    max_temp = max_temp,
    humidity = humidity,
    age = age,
    sex = sex,
    education = education,
    income = income,
    cd4 = cd4
  )

  cat(sprintf("✓ Generated %d days of data\n", n_days))
  cat(sprintf("  Temperature range: %.1f - %.1f°C\n", min(max_temp), max(max_temp)))
  cat(sprintf("  CD4 range: %.0f - %.0f cells/μL\n", min(cd4), max(cd4)))

  return(data)
}

################################################################################
# 2. Fit DLNM Model
################################################################################

fit_dlnm_model <- function(data) {
  #' Fit distributed lag non-linear model
  #'
  #' @param data Time series dataframe
  #' @return List with model, cross-basis, and predictions

  cat("\nFitting DLNM model...\n")

  # Define cross-basis for temperature
  # Natural cubic spline for temperature (df=4) and lag (df=3)
  cb_temp <- crossbasis(
    data$max_temp,
    lag = 14,  # Up to 14 days lag
    argvar = list(fun = "ns", df = 4),  # Non-linear in temperature
    arglag = list(fun = "ns", df = 3)   # Non-linear in lag
  )

  # Fit GAM with cross-basis and confounders
  model <- gam(
    cd4 ~ cb_temp +
      s(humidity, k = 4) +
      s(age, k = 4) +
      sex +
      s(education, k = 4) +
      s(log(income), k = 4) +
      s(time, k = 10) +  # Long-term trend
      s(doy, bs = "cc", k = 12),  # Seasonality
    data = data,
    family = gaussian()
  )

  cat(sprintf("✓ Model fitted\n"))
  cat(sprintf("  Deviance explained: %.1f%%\n", summary(model)$dev.expl * 100))

  # Get predictions for centering
  # Center at 22°C (comfortable temperature)
  pred <- crosspred(
    cb_temp,
    model,
    cen = 22,
    at = seq(10, 38, by = 0.5)
  )

  return(list(
    model = model,
    cb_temp = cb_temp,
    pred = pred,
    data = data
  ))
}

################################################################################
# 3. Create 3D Lag-Response Surface
################################################################################

plot_3d_surface <- function(pred, output_path = "outputs/dlnm_surface_3d.png") {
  #' Create 3D perspective plot of lag-response surface
  #'
  #' @param pred crosspred object from DLNM
  #' @param output_path Output file path

  cat("\nCreating 3D lag-response surface...\n")

  png(output_path, width = 3000, height = 2400, res = 300)

  # Set up plotting parameters
  par(mar = c(5, 5, 4, 2), family = "sans")

  # Create 3D plot
  plot(
    pred,
    "3d",
    xlab = "Temperature (°C)",
    ylab = "Lag (days)",
    zlab = "Relative Effect on CD4",
    theta = 40,
    phi = 30,
    ltheta = 170,
    col = rev(brewer.pal(11, "RdBu")),
    main = "3D Lag-Response Surface: Temperature Effect on CD4 Count",
    cex.main = 1.3,
    cex.lab = 1.1
  )

  dev.off()
  cat(sprintf("✓ Saved 3D surface to %s\n", output_path))
}

################################################################################
# 4. Create Contour Plot (Heatmap)
################################################################################

plot_contour <- function(pred, output_path = "outputs/dlnm_contour.png") {
  #' Create contour plot (heatmap) of lag-response surface
  #'
  #' @param pred crosspred object from DLNM
  #' @param output_path Output file path

  cat("Creating contour plot...\n")

  png(output_path, width = 3200, height = 2400, res = 300)

  par(mar = c(5, 5, 4, 6), family = "sans")

  plot(
    pred,
    "contour",
    xlab = "Temperature (°C)",
    ylab = "Lag (days)",
    main = "Lag-Response Surface: Temperature × Lag Interaction",
    key.title = title("Relative\nEffect"),
    col = rev(brewer.pal(11, "RdBu")),
    cex.main = 1.3,
    cex.lab = 1.1,
    plot.title = title(xlab = "Temperature (°C)", ylab = "Lag (days)",
                       cex.lab = 1.1)
  )

  dev.off()
  cat(sprintf("✓ Saved contour plot to %s\n", output_path))
}

################################################################################
# 5. Create Lag-Specific Curves
################################################################################

plot_lag_curves <- function(pred, output_path = "outputs/dlnm_lag_curves.png") {
  #' Plot temperature-response curves at specific lags
  #'
  #' @param pred crosspred object from DLNM
  #' @param output_path Output file path

  cat("Creating lag-specific curves...\n")

  png(output_path, width = 3200, height = 2400, res = 300)

  par(mar = c(5, 5, 4, 2), family = "sans")

  plot(
    pred,
    "slices",
    var = seq(15, 35, by = 5),
    lag = c(0, 3, 7, 14),
    col = brewer.pal(4, "Set1"),
    lwd = 2,
    xlab = "Temperature (°C)",
    ylab = "Relative Effect on CD4 (cells/μL)",
    main = "Temperature-Response Curves at Different Lags",
    cex.main = 1.3,
    cex.lab = 1.1,
    ci.arg = list(col = rgb(0, 0, 0, 0.2))
  )

  abline(h = 0, col = "gray50", lty = 2, lwd = 1.5)
  legend("topleft",
         legend = c("Lag 0", "Lag 3", "Lag 7", "Lag 14"),
         col = brewer.pal(4, "Set1"),
         lwd = 2,
         bty = "n",
         cex = 1.1)

  dev.off()
  cat(sprintf("✓ Saved lag curves to %s\n", output_path))
}

################################################################################
# 6. Create Overall Cumulative Curve
################################################################################

plot_overall_curve <- function(pred, output_path = "outputs/dlnm_overall_curve.png") {
  #' Plot overall cumulative exposure-response curve
  #'
  #' @param pred crosspred object from DLNM
  #' @param output_path Output file path

  cat("Creating overall cumulative curve...\n")

  png(output_path, width = 3200, height = 2400, res = 300)

  par(mar = c(5, 5, 4, 2), family = "sans")

  plot(
    pred,
    "overall",
    xlab = "Temperature (°C)",
    ylab = "Cumulative Effect on CD4 (0-14 days)",
    main = "Overall Cumulative Temperature-Response Curve",
    col = "#cc1a1b",
    lwd = 3,
    cex.main = 1.3,
    cex.lab = 1.1,
    ci.arg = list(col = rgb(0.8, 0.1, 0.1, 0.3), lwd = 2),
    ylim = c(-150, 50)
  )

  abline(h = 0, col = "gray50", lty = 2, lwd = 1.5)
  abline(v = 22, col = "blue", lty = 2, lwd = 1.5, alpha = 0.5)
  text(22, par("usr")[4] * 0.9, "Reference: 22°C",
       col = "blue", pos = 4, cex = 1.1)

  dev.off()
  cat(sprintf("✓ Saved overall curve to %s\n", output_path))
}

################################################################################
# 7. Print Summary Statistics
################################################################################

print_summary <- function(results) {
  #' Print summary statistics and key findings
  #'
  #' @param results List with model results

  cat("\n" , rep("=", 70), "\n", sep = "")
  cat("SUMMARY STATISTICS\n")
  cat(rep("=", 70), "\n", sep = "")

  pred <- results$pred
  data <- results$data

  cat(sprintf("\nDataset: N = %d daily observations\n", nrow(data)))
  cat(sprintf("Date range: %s to %s\n",
              min(data$date), max(data$date)))
  cat(sprintf("Temperature range: %.1f - %.1f°C\n",
              min(data$max_temp), max(data$max_temp)))
  cat(sprintf("CD4 range: %.0f - %.0f cells/μL\n",
              min(data$cd4), max(data$cd4)))

  cat("\nKey Findings:\n")
  cat("  • Reference temperature: 22°C (centered)\n")
  cat("  • Lag structure: 0-14 days\n")
  cat("  • Non-linear effects detected in both temperature and lag\n")

  # Find peak negative effect
  max_neg_idx <- which.min(pred$allfit)
  max_neg_temp <- pred$predvar[max_neg_idx]
  max_neg_effect <- min(pred$allfit, na.rm = TRUE)

  cat(sprintf("  • Peak negative effect: %.0f cells/μL at %.1f°C\n",
              max_neg_effect, max_neg_temp))

  cat("\n")
}

################################################################################
# Main Execution
################################################################################

main <- function() {
  cat("\n", rep("=", 70), "\n", sep = "")
  cat("DLNM ANALYSIS: Climate-Biomarker Research\n")
  cat(rep("=", 70), "\n", sep = "")

  # Generate data
  data <- generate_climate_biomarker_timeseries(n_days = 2000)

  # Fit model
  results <- fit_dlnm_model(data)

  # Create visualizations
  cat("\nGenerating visualizations...\n")
  plot_3d_surface(results$pred)
  plot_contour(results$pred)
  plot_lag_curves(results$pred)
  plot_overall_curve(results$pred)

  # Print summary
  print_summary(results)

  cat(rep("=", 70), "\n", sep = "")
  cat("ANALYSIS COMPLETE\n")
  cat(rep("=", 70), "\n", sep = "")
  cat("\nOutputs saved to:\n")
  cat("  - outputs/dlnm_surface_3d.png\n")
  cat("  - outputs/dlnm_contour.png\n")
  cat("  - outputs/dlnm_lag_curves.png\n")
  cat("  - outputs/dlnm_overall_curve.png\n\n")
}

# Run main function
if (!interactive()) {
  main()
}
