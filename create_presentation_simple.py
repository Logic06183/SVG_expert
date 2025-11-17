#!/usr/bin/env python3
"""
Create a comprehensive machine learning lecture PowerPoint presentation
Simpler version - focuses on MP4 videos and text slides
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pathlib import Path
import subprocess

# Paths
BASE_DIR = Path("/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert")
ANIMATIONS_DIR = Path("/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert_animation_export/converted_animations")
SVG_DIR = BASE_DIR / "visualization_scripts" / "outputs"
OUTPUT_FILE = Path("/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert_animation_export/ML_Training_Lecture.pptx")
PNG_DIR = Path("/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert_animation_export/png_slides")

# Create PNG directory
PNG_DIR.mkdir(exist_ok=True)

def svg_to_png(svg_path, png_path, width=1920):
    """Convert SVG to PNG using qlmanage"""
    try:
        # Use qlmanage to convert SVG to PNG
        subprocess.run([
            'qlmanage',
            '-t',
            '-s', str(width),
            '-o', str(PNG_DIR),
            str(svg_path)
        ], check=True, capture_output=True)

        # qlmanage creates filename.svg.png, rename it
        generated_png = PNG_DIR / f"{svg_path.name}.png"
        if generated_png.exists():
            generated_png.rename(png_path)
            return True
        return False
    except Exception as e:
        print(f"  Warning: Could not convert {svg_path.name}: {e}")
        return False

def add_title_slide(prs, title, subtitle=""):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    if subtitle and len(slide.placeholders) > 1:
        slide.placeholders[1].text = subtitle
    return slide

def add_content_slide(prs, title, content_path=None, content_type="image"):
    """Add a content slide with image or video"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank layout

    # Add title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.6))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.alignment = PP_ALIGN.CENTER

    # Add content
    left = Inches(0.5)
    top = Inches(1.2)
    width = Inches(9)
    height = Inches(5.8)

    if content_path and content_path.exists():
        if content_type == "video":
            slide.shapes.add_movie(str(content_path), left, top, width=width, height=height)
            print(f"  ✓ Added video: {content_path.name}")
        else:  # image
            slide.shapes.add_picture(str(content_path), left, top, width=width)
            print(f"  ✓ Added image: {content_path.name}")
    else:
        # Add placeholder text
        text_box = slide.shapes.add_textbox(left, top, width, height)
        text_frame = text_box.text_frame
        text_frame.text = f"[{title}]\n\nContent from: {content_path.name if content_path else 'N/A'}"
        text_frame.paragraphs[0].font.size = Pt(24)
        text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        print(f"  ⚠ Placeholder for: {title}")

    return slide

def convert_svg_slides():
    """Pre-convert SVG slides to PNG"""
    print("Converting SVG slides to PNG...")
    print("=" * 70)

    svg_files = [
        "session_overview.svg",
        "use_case_scenario.svg",
        "dataset_structure_example.svg",
        "data_preprocessing_pipeline.svg",
        "feature_patterns.svg",
        "how_models_learn.svg",
        "overfitting_curves.svg",
        "model_selection_flowchart.svg",
        "model_comparison_matrix.svg",
        "model_pipeline_comparison.svg",
        "model_selection_for_this_dataset.svg",
        "interpretability_spectrum.svg",
        "shap_concept.svg",
        "interpretation_workflow.svg",
        "shap_beeswarm.svg",
        "shap_dependence.svg",
        "results_comparison_dashboard.svg",
        "complete_workflow_diagram.svg"
    ]

    converted = {}
    for svg_name in svg_files:
        svg_path = SVG_DIR / svg_name
        png_path = PNG_DIR / svg_name.replace('.svg', '.png')

        if svg_path.exists():
            print(f"Converting {svg_name}...")
            if svg_to_png(svg_path, png_path):
                converted[svg_name] = png_path
            else:
                converted[svg_name] = None
        else:
            print(f"  ⚠ Not found: {svg_name}")
            converted[svg_name] = None

    print("=" * 70)
    return converted

def create_presentation():
    """Create the full presentation"""
    print("\nCreating Machine Learning Training Presentation...")
    print("=" * 70)

    # Convert SVGs first
    png_slides = convert_svg_slides()

    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # ========== SECTION 1: INTRODUCTION ==========
    print("\n[SECTION 1: Introduction]")
    add_title_slide(prs,
        "Machine Learning for Climate-Health Research",
        "A Comprehensive Training Session"
    )

    add_content_slide(prs, "Session Overview",
        content_path=png_slides.get("session_overview.svg")
    )

    add_content_slide(prs, "Use Case: Climate & Health Data",
        content_path=png_slides.get("use_case_scenario.svg")
    )

    # ========== SECTION 2: DATA & PROBLEM ==========
    print("\n[SECTION 2: Data & Problem Setup]")
    add_title_slide(prs, "Understanding Our Data", "")

    add_content_slide(prs, "Dataset Structure",
        content_path=png_slides.get("dataset_structure_example.svg")
    )

    add_content_slide(prs, "Data Preprocessing Pipeline",
        content_path=png_slides.get("data_preprocessing_pipeline.svg")
    )

    add_content_slide(prs, "Feature Patterns in the Data",
        content_path=png_slides.get("feature_patterns.svg")
    )

    # ========== SECTION 3: MODEL FUNDAMENTALS ==========
    print("\n[SECTION 3: Model Fundamentals]")
    add_title_slide(prs, "How Machine Learning Models Learn", "")

    add_content_slide(prs, "Learning Mechanisms Across Models",
        content_path=png_slides.get("how_models_learn.svg")
    )

    add_content_slide(prs, "Gradient Descent in Action",
        content_path=ANIMATIONS_DIR / "gradient_descent_animation.mp4",
        content_type="video"
    )

    # ========== SECTION 4: INDIVIDUAL MODELS ==========
    print("\n[SECTION 4: Individual Model Deep Dives]")
    add_title_slide(prs, "Decision Trees & Ensembles", "")

    add_content_slide(prs, "How Decision Trees Build",
        content_path=ANIMATIONS_DIR / "decision_tree_building.mp4",
        content_type="video"
    )

    add_content_slide(prs, "Random Forest: Ensemble Power",
        content_path=ANIMATIONS_DIR / "random_forest_ensemble.mp4",
        content_type="video"
    )

    add_content_slide(prs, "Gradient Boosting: Sequential Learning",
        content_path=ANIMATIONS_DIR / "gradient_boosting_sequence.mp4",
        content_type="video"
    )

    add_title_slide(prs, "Neural Networks", "")

    add_content_slide(prs, "Backpropagation Flow",
        content_path=ANIMATIONS_DIR / "backpropagation_flow.mp4",
        content_type="video"
    )

    # ========== SECTION 5: KEY CONCEPTS ==========
    print("\n[SECTION 5: Key ML Concepts]")
    add_title_slide(prs, "Critical Concepts in ML", "")

    add_content_slide(prs, "Bias-Variance Tradeoff",
        content_path=ANIMATIONS_DIR / "bias_variance_tradeoff.mp4",
        content_type="video"
    )

    add_content_slide(prs, "Overfitting Behavior Across Models",
        content_path=png_slides.get("overfitting_curves.svg")
    )

    add_content_slide(prs, "The Double Descent Phenomenon",
        content_path=ANIMATIONS_DIR / "double_descent_phenomenon.mp4",
        content_type="video"
    )

    add_content_slide(prs, "Learning Rate Effects",
        content_path=ANIMATIONS_DIR / "learning_rate_effect.mp4",
        content_type="video"
    )

    # ========== SECTION 6: HYPERPARAMETER TUNING ==========
    print("\n[SECTION 6: Hyperparameter Tuning]")
    add_title_slide(prs, "Optimizing Model Performance", "")

    add_content_slide(prs, "Tree Depth Impact",
        content_path=ANIMATIONS_DIR / "hyperparameter_tuning_tree_depth.mp4",
        content_type="video"
    )

    add_content_slide(prs, "Regularization Effects",
        content_path=ANIMATIONS_DIR / "hyperparameter_tuning_regularization.mp4",
        content_type="video"
    )

    # ========== SECTION 7: MODEL SELECTION ==========
    print("\n[SECTION 7: Model Selection & Comparison]")
    add_title_slide(prs, "Choosing the Right Model", "")

    add_content_slide(prs, "Model Selection Flowchart",
        content_path=png_slides.get("model_selection_flowchart.svg")
    )

    add_content_slide(prs, "Comprehensive Model Comparison",
        content_path=png_slides.get("model_comparison_matrix.svg")
    )

    add_content_slide(prs, "Model Pipeline Comparison",
        content_path=png_slides.get("model_pipeline_comparison.svg")
    )

    add_content_slide(prs, "Model Selection for This Dataset",
        content_path=png_slides.get("model_selection_for_this_dataset.svg")
    )

    # ========== SECTION 8: INTERPRETABILITY ==========
    print("\n[SECTION 8: Model Interpretability]")
    add_title_slide(prs, "Understanding Model Predictions", "")

    add_content_slide(prs, "The Interpretability Spectrum",
        content_path=png_slides.get("interpretability_spectrum.svg")
    )

    add_content_slide(prs, "SHAP: Bridging the Gap",
        content_path=png_slides.get("shap_concept.svg")
    )

    add_content_slide(prs, "Feature Importance Evolution",
        content_path=ANIMATIONS_DIR / "feature_importance_buildup.mp4",
        content_type="video"
    )

    add_content_slide(prs, "SHAP Interpretation Workflow",
        content_path=png_slides.get("interpretation_workflow.svg")
    )

    add_content_slide(prs, "SHAP Beeswarm Plot",
        content_path=png_slides.get("shap_beeswarm.svg")
    )

    add_content_slide(prs, "SHAP Dependence Analysis",
        content_path=png_slides.get("shap_dependence.svg")
    )

    # ========== SECTION 9: RESULTS ==========
    print("\n[SECTION 9: Results & Conclusions]")
    add_title_slide(prs, "Results & Recommendations", "")

    add_content_slide(prs, "Results Comparison Dashboard",
        content_path=png_slides.get("results_comparison_dashboard.svg")
    )

    add_content_slide(prs, "Complete Workflow",
        content_path=png_slides.get("complete_workflow_diagram.svg")
    )

    # Final slide
    add_title_slide(prs, "Thank You!", "Questions?")

    # Save presentation
    print("\n" + "=" * 70)
    print(f"Saving presentation to: {OUTPUT_FILE}")
    prs.save(str(OUTPUT_FILE))
    print(f"✓ Presentation created successfully!")
    print(f"  Total slides: {len(prs.slides)}")
    print(f"  Location: {OUTPUT_FILE}")
    print("=" * 70)

    return OUTPUT_FILE

if __name__ == "__main__":
    output_path = create_presentation()
    print(f"\n✓ Done! Open with: open \"{output_path}\"")
