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

## Installation

1. Create a virtual environment:
```bash
uv venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
uv pip install mflux streamlit pillow
```

## Usage

1. Activate the virtual environment:
```bash
source .venv/bin/activate
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Notes

- The first time you run the app, it will download the model weights (~34GB for each model)
- Higher resolution and more steps will result in longer generation times
- Generated images are saved in the `generated_images` directory
