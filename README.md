# Local AI Image Gen Template

This templates develops and spins up a Streamlit-based user interface for the mflux AI image generator, providing an intuitive way to generate AI images using various models and parameters.

## Overview

This application wraps the mflux-generate CLI tool in a user-friendly web interface, allowing users to:
- Select different AI models (schnell/dev)
- Configure generation parameters
- Generate images from text prompts
- Download generated images
- Experiment with advanced parameters like negative prompts and sampling methods

## Potential app functionality expansions to explore

Here are some ideas of how to expand this template after you get it up and running:
- Allow user to select the number of images the generator should create
- Add a dropdown with potential image styles
- Add a share button for direct social media sharing

## Requirements

- macOS 11.0 or later
- Apple Silicon Mac (M1/M2/M3)
- Python 3.11+
- ~40GB free disk space for models
- 16GB+ RAM recommended
- CUDA-capable GPU recommended (but not required)

## Technology Stack

- [Streamlit](https://streamlit.io/) - Web interface framework
- [mflux](https://github.com/mflux/mflux) - AI image generation backend
- [Pillow](https://python-pillow.org/) - Image processing
- [uv](https://github.com/astral-sh/uv) - Python package manager and virtual environment tool

## Quick Start

Just ask Memex to run this app locally and it will take care of the rest! If you run into any errors, just point Memex to fix them.

If you’d like to set up the environment and dependencies manually, follow these steps:

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install streamlit~=1.42.0 pillow~=10.4.0 mflux~=0.5.1

# Start the app
uv run -m streamlit run app.py
```

Visit http://localhost:8501 in your browser.

## First Run Notes

- First model download is ~34GB
- Initial model load takes 3-5 minutes
- Models are cached in `~/.cache/mflux/`
- Start with "schnell" model for faster testing

## Development

See Rules for AI (rendered from `.memex/rules.md`) for detailed development guidelines Memex will follow, including:
- Complete setup instructions
- Model-specific parameters
- Error handling
- Potential improvements
- Development workflow

You can ask Memex to update rules.md to reflect your project needs as you expand it, or set it as part of your Custom Instructions so that it does it automatically after important steps.

## License

MIT License - See LICENSE file for details
