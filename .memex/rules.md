# AI Image Generator UI - Agent Guide

## Project Context
- Base project: mflux AI image generator with Streamlit UI
- Original repo: https://github.com/mflux/mflux (fetch this for latest API docs)
- Architecture: Streamlit UI wrapping mflux-generate CLI

## Initial Setup
1. **Virtual Environment Setup**
   ```python
   # Create and activate virtual environment
   uv venv
   source .venv/bin/activate

   # Install core dependencies
   uv pip install streamlit~=1.42.0 pillow~=10.4.0
   
   # Install mflux - this will also install the CLI tool
   uv pip install mflux~=0.5.1
   
   # Verify mflux-generate is available
   mflux-generate --help
   ```

   Note: Despite app.py containing dependency specs, explicit installation ensures CLI tools are properly installed in PATH

2. **First Run Considerations**
   - First model download is ~34GB
   - Models are cached in ~/.cache/mflux/
   - Ensure sufficient disk space
   - Initial model load takes 3-5 minutes

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

## Development Loop
1. **Local Development Setup**
   ```python
   # Run app with auto-reload
   uv run -m streamlit run app.py
   ```

2. **Effective Iteration**
   - Browser updates automatically on code changes
   - Generated images saved to `generated_images/` with timestamp
   - Keep browser and terminal side by side for quick feedback
   - Subsequent model loads are faster (cached)

## mflux-specific Tasks

1. **Custom Model Loading**
   ```python
   # Add to cmd list before generation
   cmd.extend(["--model-path", "/path/to/custom/model"])
   ```

2. **Advanced Generation Control**
   ```python
   # Negative prompts (things to avoid in generation)
   cmd.extend(["--negative-prompt", "bad quality, blurry"])
   
   # Control over inference
   cmd.extend(["--sampler", "euler_a"])  # Different sampling methods
   cmd.extend(["--cfg-scale", "7.5"])    # Classifier free guidance
   ```

3. **Batch Generation**
   ```python
   # Generate variations with same prompt
   cmd.extend(["--n-samples", "4"])
   ```

## Potential Improvements

1. **Generation Features**
   - Image-to-image generation support
   - Inpainting/outpainting capabilities
   - Prompt templates/presets
   - Style transfer options
   - Face enhancement integration

2. **UI Enhancements**
   - Gallery view of generated images
   - Generation history
   - Prompt history/favorites
   - Parameter presets
   - Batch generation interface

3. **Performance Optimizations**
   - Model caching
   - Progressive image preview
   - Queue system for batch jobs
   - Memory-efficient batch processing

4. **Advanced Features**
   - Prompt engineering assistance
   - Style mixing
   - Animation generation
   - Upscaling integration
   - Automatic face correction

## Error Handling
Specific to mflux-generate:
1. Model loading failures:
   ```python
   try:
       result = subprocess.run(cmd, capture_output=True, text=True)
       if "Error loading model" in result.stderr:
           st.error("Model failed to load. Check disk space and permissions.")
   except Exception as e:
       st.error(f"Generation failed: {str(e)}")
   ```

2. CUDA/Memory issues:
   ```python
   if "CUDA out of memory" in result.stderr:
       st.error("Memory limit reached. Try reducing resolution or batch size.")
   ```

3. Common mflux-specific errors:
   - "Model not found": Check ~/.cache/mflux/ permissions
   - "CUDA initialization failed": Verify GPU availability
   - "Invalid sampler": Check mflux-generate --help for valid options
