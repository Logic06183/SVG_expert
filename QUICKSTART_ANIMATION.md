# Animation Export - Quick Start Guide

Get your SVG animations into PowerPoint in 3 easy steps!

## Step 1: Install Dependencies (One-time setup)

```bash
# Install system tools
brew install ffmpeg chromedriver gifsicle

# Install Python packages
pip3 install -r requirements.txt
```

## Step 2: Convert Your Animations

### Option A: Convert All Animations

```bash
./convert_all.sh
```

This will convert all ML training animations to both MP4 and GIF formats.

### Option B: Convert Specific Animation

```bash
./convert_animations.py visualization_scripts/outputs/animations/gradient_descent_animation.svg
```

## Step 3: Use in PowerPoint

### For MP4 Videos:
1. Open PowerPoint
2. Go to **Insert** → **Video** → **Video from File**
3. Select your `.mp4` file from `converted_animations/`
4. Done! Video will play in your presentation

### For GIF Animations:
1. Open PowerPoint
2. Go to **Insert** → **Pictures** → **Picture from File**
3. Select your `.gif` file from `converted_animations/`
4. Done! GIF will loop automatically

## Available Animations

Located in `visualization_scripts/outputs/animations/`:

- `gradient_descent_animation.svg` - How gradient descent finds optimal solutions
- `decision_tree_building.svg` - Building decision trees step by step
- `random_forest_ensemble.svg` - Random forest ensemble learning
- `backpropagation_flow.svg` - Neural network backpropagation
- `learning_rate_effect.svg` - Effect of learning rate on training
- `feature_importance_buildup.svg` - Feature importance accumulation
- `bias_variance_tradeoff.svg` - Bias-variance tradeoff visualization
- `gradient_boosting_sequence.svg` - Gradient boosting step by step
- `hyperparameter_tuning_tree_depth.svg` - Effect of tree depth
- `hyperparameter_tuning_regularization.svg` - Regularization effects
- `double_descent_phenomenon.svg` - Double descent in model complexity

## Tips

- **First time?** Start with one animation to test your setup
- **Quality matters?** Use `--fps 60` for smoother animations
- **File size?** MP4 files are smaller, GIFs are more compatible
- **Wrong duration?** Adjust with `--duration N` (seconds)

## Need Help?

Check the full README_ANIMATION.md for:
- Troubleshooting common issues
- Advanced customization options
- Detailed command reference

## Going Back to Main Repository

```bash
cd ../SVG_expert
```

---

**Ready to make your presentations dynamic!** 🎬
