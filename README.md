# AI Image Generator UI

A Streamlit-based user interface for generating AI images using mflux.

## Features

- Support for both schnell and dev models
- Adjustable generation parameters:
  - Model selection (schnell/dev)
  - Quantization (None, 4-bit, 8-bit)
  - Number of steps
  - Guidance scale (for dev model)
  - Seed control
  - Resolution selection
- Image download capability
- Progress indicators
- Error handling

## Requirements

- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- Python 3.11+

## Installation & Running

```bash
# Clone the repository
git clone https://github.com/yourusername/ai_image_generator_ui_mflux.git
cd ai_image_generator_ui_mflux

# Run the app (uv will handle dependencies automatically)
uv run -m streamlit run app.py
```

The app will be available at http://localhost:8501

## Notes

- First run will download model weights (~34GB for each model)
- Higher resolution and more steps will result in longer generation times
- Generated images are saved in the `generated_images` directory
