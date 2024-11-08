import streamlit as st
from PIL import Image, ImageOps
from rembg import remove
import io

def remove_bg(image):
    # input_img = "img3.png"
    # output_img = "img.png"
    # inp = Image.open(image)
    output = remove(image , alpha_matting=True)
    # output.save(output_img)
    return output

def add_bg_color(foreground, color):
    # Create a background image with the specified color
    background = Image.new('RGBA', foreground.size, color)
    
    # Combine the foreground and background
    combined = Image.alpha_composite(background, foreground)
    
    return combined

def add_bg_image(foreground, background):
    # Ensure the background is the same size as the foreground
    background = background.resize(foreground.size)
    
    # Create a new image by blending the foreground and background
    combined = Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA'))
    
    return combined

def main():
    st.title("Background Remover and Color Adder")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        bg_color = st.color_picker('Pick A Background Color', '#ffffff')
        bg_image_file = st.file_uploader("Choose a background image...", type=["jpg", "png", "jpeg"])
        col1, col2 = st.columns(2)
        
        if 'output' not in st.session_state:
            st.session_state.output = None
        if 'output_with_bg' not in st.session_state:
            st.session_state.output_with_bg = None
        
        with col1:
            if st.button('Remove Background'):
                st.balloons()
                st.session_state.output = remove_bg(image)
                
            if st.session_state.output is not None:
                st.write("Right Click and Save Image on PC/ Long press and save image on mobile")
                st.image(st.session_state.output, caption='Output Image.', use_column_width=True)
                
                # Convert output image to bytes
                buf = io.BytesIO()
                st.session_state.output.save(buf, format="PNG")
                st.session_state.byte_im = buf.getvalue()
                
                st.download_button(
                    label="Download Transparent Image",
                    data=st.session_state.byte_im,
                    file_name="transparent_image.png",
                    mime="image/png"
                )
        
        with col2:
            if st.session_state.output is not None:
                if bg_image_file is not None:
                    bg_image = Image.open(bg_image_file)
                    st.session_state.output_with_bg = add_bg_image(st.session_state.output, bg_image)
                else:
                    st.session_state.output_with_bg = add_bg_color(st.session_state.output, bg_color)
                
                st.write("Right Click and Save Image on PC/ Long press and save image on mobile")
                st.image(st.session_state.output_with_bg, caption='Output Image with Background.', use_column_width=True)
                
                # Convert output_with_bg image to bytes
                buf = io.BytesIO()
                st.session_state.output_with_bg.save(buf, format="PNG")
                st.session_state.byte_im_with_bg = buf.getvalue()
                
                st.download_button(
                    label="Download Image with Background",
                    data=st.session_state.byte_im_with_bg,
                    file_name="image_with_background.png",
                    mime="image/png"
                )

    st.sidebar.title("About")
    st.sidebar.info(
        "This is a simple web app to remove background from images. It uses the rembg library."
    )
    st.sidebar.title("Github")
    st.sidebar.info(
        "This web app is maintained by [Anurag Singh](https://github.com/anurag-singh-9622/)"
    )

if __name__ == "__main__":
    main()