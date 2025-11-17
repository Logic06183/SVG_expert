#!/usr/bin/env python3
"""
Create a comprehensive machine learning lecture PowerPoint presentation
Combines static visualizations and animated MP4s
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path
import cairosvg
from io import BytesIO

# Paths
BASE_DIR = Path("/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert")
ANIMATIONS_DIR = Path("/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert_animation_export/converted_animations")
SVG_DIR = BASE_DIR / "visualization_scripts" / "outputs"
OUTPUT_FILE = Path("/Users/craig/Library/Mobile Documents/com~apple~CloudDocs/SVG_expert_animation_export/ML_Training_Lecture.pptx")

def svg_to_png_bytes(svg_path):
    """Convert SVG to PNG bytes for embedding"""
    try:
        png_bytes = cairosvg.svg2png(url=str(svg_path), output_width=1920)
        return BytesIO(png_bytes)
    except Exception as e:
        print(f"Error converting {svg_path}: {e}")
        return None

def add_title_slide(prs, title, subtitle=""):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[0])  # Title slide layout
    slide.shapes.title.text = title
    if subtitle and len(slide.placeholders) > 1:
        slide.placeholders[1].text = subtitle
    return slide

def add_content_slide(prs, title, svg_path=None, mp4_path=None):
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

    if svg_path and svg_path.exists():
        png_bytes = svg_to_png_bytes(svg_path)
        if png_bytes:
            slide.shapes.add_picture(png_bytes, left, top, width=width)
            print(f"  Added SVG: {svg_path.name}")

    elif mp4_path and mp4_path.exists():
        slide.shapes.add_movie(str(mp4_path), left, top, width=width, height=height)
        print(f"  Added MP4: {mp4_path.name}")

    return slide

def create_presentation():
    """Create the full presentation"""
    print("Creating Machine Learning Training Presentation...")
    print("=" * 70)

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
        svg_path=SVG_DIR / "session_overview.svg"
    )

    add_content_slide(prs, "Use Case: Climate & Health Data",
        svg_path=SVG_DIR / "use_case_scenario.svg"
    )

    # ========== SECTION 2: DATA & PROBLEM ==========
    print("\n[SECTION 2: Data & Problem Setup]")
    add_title_slide(prs, "Understanding Our Data", "")

    add_content_slide(prs, "Dataset Structure",
        svg_path=SVG_DIR / "dataset_structure_example.svg"
    )

    add_content_slide(prs, "Data Preprocessing Pipeline",
        svg_path=SVG_DIR / "data_preprocessing_pipeline.svg"
    )

    add_content_slide(prs, "Feature Patterns in the Data",
        svg_path=SVG_DIR / "feature_patterns.svg"
    )

    # ========== SECTION 3: MODEL FUNDAMENTALS ==========
    print("\n[SECTION 3: Model Fundamentals]")
    add_title_slide(prs, "How Machine Learning Models Learn", "")

    add_content_slide(prs, "Learning Mechanisms Across Models",
        svg_path=SVG_DIR / "how_models_learn.svg"
    )

    add_content_slide(prs, "Gradient Descent in Action",
        mp4_path=ANIMATIONS_DIR / "gradient_descent_animation.mp4"
    )

    # ========== SECTION 4: INDIVIDUAL MODELS ==========
    print("\n[SECTION 4: Individual Model Deep Dives]")
    add_title_slide(prs, "Decision Trees & Ensembles", "")

    add_content_slide(prs, "How Decision Trees Build",
        mp4_path=ANIMATIONS_DIR / "decision_tree_building.mp4"
    )

    add_content_slide(prs, "Random Forest: Ensemble Power",
        mp4_path=ANIMATIONS_DIR / "random_forest_ensemble.mp4"
    )

    add_content_slide(prs, "Gradient Boosting: Sequential Learning",
        mp4_path=ANIMATIONS_DIR / "gradient_boosting_sequence.mp4"
    )

    add_title_slide(prs, "Neural Networks", "")

    add_content_slide(prs, "Backpropagation Flow",
        mp4_path=ANIMATIONS_DIR / "backpropagation_flow.mp4"
    )

    # ========== SECTION 5: KEY CONCEPTS ==========
    print("\n[SECTION 5: Key ML Concepts]")
    add_title_slide(prs, "Critical Concepts in ML", "")

    add_content_slide(prs, "Bias-Variance Tradeoff",
        mp4_path=ANIMATIONS_DIR / "bias_variance_tradeoff.mp4"
    )

    add_content_slide(prs, "Overfitting Behavior Across Models",
        svg_path=SVG_DIR / "overfitting_curves.svg"
    )

    add_content_slide(prs, "The Double Descent Phenomenon",
        mp4_path=ANIMATIONS_DIR / "double_descent_phenomenon.mp4"
    )

    add_content_slide(prs, "Learning Rate Effects",
        mp4_path=ANIMATIONS_DIR / "learning_rate_effect.mp4"
    )

    # ========== SECTION 6: HYPERPARAMETER TUNING ==========
    print("\n[SECTION 6: Hyperparameter Tuning]")
    add_title_slide(prs, "Optimizing Model Performance", "")

    add_content_slide(prs, "Tree Depth Impact",
        mp4_path=ANIMATIONS_DIR / "hyperparameter_tuning_tree_depth.mp4"
    )

    add_content_slide(prs, "Regularization Effects",
        mp4_path=ANIMATIONS_DIR / "hyperparameter_tuning_regularization.mp4"
    )

    # ========== SECTION 7: MODEL SELECTION ==========
    print("\n[SECTION 7: Model Selection & Comparison]")
    add_title_slide(prs, "Choosing the Right Model", "")

    add_content_slide(prs, "Model Selection Flowchart",
        svg_path=SVG_DIR / "model_selection_flowchart.svg"
    )

    add_content_slide(prs, "Comprehensive Model Comparison",
        svg_path=SVG_DIR / "model_comparison_matrix.svg"
    )

    add_content_slide(prs, "Model Pipeline Comparison",
        svg_path=SVG_DIR / "model_pipeline_comparison.svg"
    )

    add_content_slide(prs, "Model Selection for This Dataset",
        svg_path=SVG_DIR / "model_selection_for_this_dataset.svg"
    )

    # ========== SECTION 8: INTERPRETABILITY ==========
    print("\n[SECTION 8: Model Interpretability]")
    add_title_slide(prs, "Understanding Model Predictions", "")

    add_content_slide(prs, "The Interpretability Spectrum",
        svg_path=SVG_DIR / "interpretability_spectrum.svg"
    )

    add_content_slide(prs, "SHAP: Bridging the Gap",
        svg_path=SVG_DIR / "shap_concept.svg"
    )

    add_content_slide(prs, "Feature Importance Evolution",
        mp4_path=ANIMATIONS_DIR / "feature_importance_buildup.mp4"
    )

    add_content_slide(prs, "SHAP Interpretation Workflow",
        svg_path=SVG_DIR / "interpretation_workflow.svg"
    )

    add_content_slide(prs, "SHAP Beeswarm Plot",
        svg_path=SVG_DIR / "shap_beeswarm.svg"
    )

    add_content_slide(prs, "SHAP Dependence Analysis",
        svg_path=SVG_DIR / "shap_dependence.svg"
    )

    # ========== SECTION 9: RESULTS ==========
    print("\n[SECTION 9: Results & Conclusions]")
    add_title_slide(prs, "Results & Recommendations", "")

    add_content_slide(prs, "Results Comparison Dashboard",
        svg_path=SVG_DIR / "results_comparison_dashboard.svg"
    )

    add_content_slide(prs, "Complete Workflow",
        svg_path=SVG_DIR / "complete_workflow_diagram.svg"
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

if __name__ == "__main__":
    create_presentation()
