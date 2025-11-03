# Setup Checklist for Animation Export

Complete these steps to start converting animations.

## ☐ System Dependencies

### Required:

```bash
# FFmpeg (video encoding)
brew install ffmpeg

# ChromeDriver (browser automation for rendering)
brew install chromedriver
```

### Optional but Recommended:

```bash
# Gifsicle (GIF optimization)
brew install gifsicle
```

**Verify installation:**
```bash
ffmpeg -version
chromedriver --version
gifsicle --version  # optional
```

## ☐ Python Dependencies

```bash
# Install required Python packages
pip3 install -r requirements.txt
```

**This installs:**
- `selenium` - Browser automation
- `Pillow` - Image processing
- `webdriver-manager` - ChromeDriver management

## ☐ Script Permissions

Already done! Scripts are executable:
- ✅ `convert_animations.py`
- ✅ `convert_all.sh`

## ☐ Test Your Setup

Run a test conversion:

```bash
./convert_animations.py \
    --duration 5 \
    --fps 30 \
    visualization_scripts/outputs/animations/gradient_descent_animation.svg
```

**Expected output:**
- Captures 150 frames (5 seconds × 30 fps)
- Creates `gradient_descent_animation.mp4`
- Creates `gradient_descent_animation.gif`
- Files saved in `converted_animations/`

## ☐ Troubleshooting macOS Security

If you get security warnings for ChromeDriver:

```bash
xattr -d com.apple.quarantine $(which chromedriver)
```

Or go to **System Preferences** → **Security & Privacy** and allow it to run.

## Ready to Go?

Once all checkboxes are complete:

1. Run `./convert_all.sh` to convert all animations
2. Or convert specific files with `./convert_animations.py <file>`
3. Find your MP4 and GIF files in `converted_animations/`
4. Insert them into your PowerPoint presentations!

---

**Having issues?** Check README_ANIMATION.md for detailed troubleshooting.
