# AI Image Generator UI

A Streamlit-based user interface for the mflux AI image generator, providing an intuitive way to generate AI images using various models and parameters.

## Overview

This application wraps the mflux-generate CLI tool in a user-friendly web interface, allowing users to:
- Select different AI models (schnell/dev)
- Configure generation parameters
- Generate images from text prompts
- Download generated images
- Experiment with advanced parameters like negative prompts and sampling methods

## Technology Stack

- [Streamlit](https://streamlit.io/) - Web interface framework
- [mflux](https://github.com/mflux/mflux) - AI image generation backend
- [Pillow](https://python-pillow.org/) - Image processing
- [uv](https://github.com/astral-sh/uv) - Python package manager and virtual environment tool

## Quick Start

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
- Models are cached in ~/.cache/mflux/
- Start with "schnell" model for faster testing

## Development

See [.memex/rules.md](.memex/rules.md) for detailed development guidelines including:
- Complete setup instructions
- Model-specific parameters
- Error handling
- Potential improvements
- Development workflow

## Requirements

- Python 3.11+
- ~40GB free disk space for models
- 16GB+ RAM recommended
- CUDA-capable GPU recommended (but not required)

## License

MIT License

Copyright (c) 2025 Atlas Futures Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
