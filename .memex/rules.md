# AI Image Generator UI - Development Guide

## Overview
This project provides a Streamlit UI for mflux's image generation capabilities. The architecture is simple:
- Single `app.py` file containing UI and generation logic
- Uses mflux-generate CLI for image generation
- Streamlit for web interface
- uv for dependency management

## Key Components
1. **UI Layer** (Streamlit)
   - Handles parameter input
   - Displays generated images
   - Manages download functionality

2. **Generation Layer** (mflux-generate)
   - Executes image generation via CLI
   - Handles model loading and inference
   - Manages output file creation

## Development Workflow

### Setting Up Development Environment
```bash
git clone <repository>
cd ai_image_generator_ui_mflux
uv run -m streamlit run app.py
```

### Making Changes
1. **UI Modifications**
   - All UI elements are in `app.py`
   - Streamlit components are organized by sidebar/main area
   - Changes auto-reload in browser

2. **Adding Features**
   - New generation parameters: Add to sidebar section
   - New output options: Add to generation result section
   - New CLI options: Add to cmd list in generate section

3. **Testing Changes**
   - Run app locally: `uv run -m streamlit run app.py`
   - Test different parameter combinations
   - Verify image generation and download

### Best Practices
1. **Code Organization**
   - Keep UI logic separate from generation logic
   - Use clear variable names for parameters
   - Add comments for complex parameter interactions

2. **Error Handling**
   - Always wrap mflux-generate calls in try/except
   - Provide clear error messages to users
   - Log errors for debugging

3. **Performance**
   - Use appropriate default values for parameters
   - Consider adding caching for repeated operations
   - Monitor memory usage with large models

### Common Tasks
1. **Adding a New Parameter**
   ```python
   new_param = st.sidebar.slider(
       "Parameter Name",
       min_value=0,
       max_value=100,
       value=50,
       help="Parameter description"
   )
   cmd.extend(["--new-param", str(new_param)])
   ```

2. **Adding Output Options**
   ```python
   if st.checkbox("Show additional info"):
       st.write("Additional generation details...")
   ```

3. **Modifying Generation Settings**
   ```python
   # Add to cmd list in generate section
   if special_option:
       cmd.extend(["--special-option", "value"])
   ```

### Deployment
1. **Local Development**
   - Use `uv run -m streamlit run app.py`
   - Access at http://localhost:8501

2. **Production**
   - Consider using Streamlit Cloud
   - Or deploy with Docker (add Dockerfile)
   - Ensure model weights are properly cached

### Troubleshooting
1. **Common Issues**
   - Model download failures: Check network/disk space
   - Memory errors: Reduce batch size/resolution
   - UI not updating: Check Streamlit cache

2. **Debug Tools**
   - Use st.write() for debugging
   - Check streamlit logs
   - Monitor system resources
