# /// script
# dependencies = [
#   "streamlit~=1.42.0",
#   "pillow~=10.4.0",
#   "mflux~=0.5.1"
# ]
# ///

import streamlit as st
import subprocess
import os
import time
from PIL import Image

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

st.title("AI Image Generator")

# Sidebar controls
with st.sidebar:
    st.header("Generation Settings")
    
    model_name = st.selectbox(
        "Select Model",
        ["schnell", "dev"],
        help="schnell is faster but dev might produce better quality images"
    )
    
    quantize = st.selectbox(
        "Quantization",
        [None, 4, 8],
        format_func=lambda x: "None" if x is None else f"{x}-bit",
        help="Lower bits = faster generation but might affect quality"
    )
    
    steps = st.slider(
        "Steps",
        min_value=2,
        max_value=25,
        value=4 if model_name == "schnell" else 20,
        help="More steps = better quality but slower generation"
    )
    
    if model_name == "dev":
        guidance = st.slider(
            "Guidance Scale",
            min_value=1.0,
            max_value=10.0,
            value=3.5,
            step=0.5,
            help="Higher values = stronger adherence to prompt"
        )
    
    seed = st.number_input(
        "Seed",
        min_value=0,
        max_value=999999999,
        value=42,
        help="Same seed + same settings = same image"
    )
    
    resolution = st.select_slider(
        "Resolution",
        options=[512, 768, 1024],
        value=1024,
        help="Higher resolution = better quality but slower generation"
    )

# Main content
prompt = st.text_area(
    "Enter your prompt",
    height=100,
    placeholder="Describe the image you want to generate..."
)

if st.button("Generate Image", type="primary"):
    if not prompt:
        st.error("Please enter a prompt first!")
    else:
        try:
            # Prepare command
            cmd = ["mflux-generate", 
                  "--model", model_name,
                  "--prompt", prompt,
                  "--seed", str(seed),
                  "--steps", str(steps),
                  "--height", str(resolution),
                  "--width", str(resolution)]
            
            # Add quantization if selected
            if quantize is not None:
                cmd.extend(["--quantize", str(quantize)])
            
            # Add guidance for dev model
            if model_name == "dev":
                cmd.extend(["--guidance", str(guidance)])
            
            # Set output path
            output_dir = "generated_images"
            os.makedirs(output_dir, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{output_dir}/image_{timestamp}.png"
            cmd.extend(["--output", filename])
            
            # Generate image
            with st.spinner("Generating image..."):
                start_time = time.time()
                result = subprocess.run(cmd, capture_output=True, text=True)
                generation_time = time.time() - start_time
                
                if result.returncode != 0:
                    raise Exception(f"Command failed: {result.stderr}")
            
            # Display results
            st.success(f"Image generated in {generation_time:.2f} seconds!")
            
            # Display image
            image = Image.open(filename)
            st.image(image, caption=prompt, use_column_width=True)
            
            # Download button
            with open(filename, "rb") as file:
                st.download_button(
                    label="Download Image",
                    data=file,
                    file_name=f"ai_generated_{timestamp}.png",
                    mime="image/png"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("AI Image Generator UI")
        print("Usage: uv run app.py")
        print("This will start a Streamlit server with the UI")
        sys.exit(0)
