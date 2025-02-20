import streamlit as st
from mflux import Flux1, Config
from PIL import Image
import os
import time

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
            with st.spinner("Loading model..."):
                # Initialize model
                flux = Flux1.from_name(
                    model_name=model_name,
                    quantize=quantize
                )
            
            # Configure generation parameters
            config = Config(
                num_inference_steps=steps,
                height=resolution,
                width=resolution,
            )
            
            if model_name == "dev":
                config.guidance_scale = guidance
            
            # Generate image
            with st.spinner("Generating image..."):
                start_time = time.time()
                image = flux.generate_image(
                    seed=seed,
                    prompt=prompt,
                    config=config
                )
                generation_time = time.time() - start_time
            
            # Display results
            st.success(f"Image generated in {generation_time:.2f} seconds!")
            
            # Save image
            output_dir = "generated_images"
            os.makedirs(output_dir, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{output_dir}/image_{timestamp}.png"
            image.save(filename)
            
            # Display image
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
