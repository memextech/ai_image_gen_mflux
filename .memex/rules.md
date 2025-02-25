# AI Image Generator UI - Agent Guide

## Project Context
- Base project: mflux AI image generator with Streamlit UI
- Original repo: https://github.com/mflux/mflux (fetch this for latest API docs)
- Architecture: Streamlit UI wrapping mflux-generate CLI

## Running the App From Scratch

1. **Environment Setup**
   ```python
   # Create and activate virtual environment
   uv venv
   source .venv/bin/activate

   # Install core dependencies
   uv pip install streamlit~=1.42.0 pillow~=10.4.0

   # Install mflux - this will also install the CLI tool
   uv pip install mflux~=0.5.1
   ```

2. **Verify Installation**
   ```python
   # Verify mflux-generate is available
   mflux-generate --help

   # Should show available models and commands
   ```
3. Download smaller 4bit quantized models from huggingface first before running.
- Download this model `madroid/flux.1-schnell-mflux-4bit` from hugging face
- Then use the locally downloaded model via this flag `--path local-model-directory`

4. **Start the App**
   ```python
   # Run with auto-reload enabled
   uv run -m streamlit run app.py
   ```

5. **First Run Process**
   - Browser will open to http://localhost:8501
   - Select model (start with "schnell" for faster testing)
   - Wait 3-5 minutes for initial model load
   - Models are cached in ~/.cache/mflux/ for subsequent runs

## Core Components
1. **Generation Interface**
   - Uses mflux-generate CLI (not Python API)
   - Command structure:
     ```python
     cmd = ["mflux-generate",
            "--model", model_name,      # "schnell" or "dev"
            "--prompt", prompt,         # text prompt
            "--seed", str(seed),        # reproducibility
            "--steps", str(steps),      # quality vs speed
            "--height", str(height),    # image dimensions
            "--width", str(width)]
     ```

2. **Model-Specific Parameters**
   - schnell: Faster generation, fewer parameters
   - dev: Higher quality, additional parameters:
     - guidance: Controls prompt adherence (1.0-10.0)
     - More steps recommended (15-25)

## mflux-specific Tasks

1. **Custom Model Loading**
   ```python
   # Add to cmd list before generation
   cmd.extend(["--path", "/path/to/custom/model"])
   ```
