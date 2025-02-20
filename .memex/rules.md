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

3. **Start the App**
   ```python
   # Run with auto-reload enabled
   uv run -m streamlit run app.py
   ```

4. **First Run Process**
   - Browser will open to http://localhost:8501
   - Select model (start with "schnell" for faster testing)
   - First generation will trigger model download (~34GB)
   - Wait 3-5 minutes for initial model load
   - Models are cached in ~/.cache/mflux/ for subsequent runs

5. **Development Loop**
   - Keep browser and terminal side by side
   - Code changes trigger automatic UI updates
   - Generated images appear in `generated_images/` directory
   - Subsequent model loads are much faster

6. **Testing the Setup**
   ```python
   # Basic test prompt
   prompt = "a photo of a cat"
   steps = 15  # Start with lower steps for faster generation
   width = 512
   height = 512
   ```

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
