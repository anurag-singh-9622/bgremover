import streamlit as st
from PIL import Image, ImageOps
from rembg import remove
import io
import requests

def remove_bg(image):
    output = remove(image , alpha_matting=True)
    return output

def add_bg_color(foreground, color):
    background = Image.new('RGBA', foreground.size, color)
    combined = Image.alpha_composite(background, foreground)
    return combined

def add_bg_image(foreground, background):
    background = background.resize(foreground.size)
    combined = Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA'))
    return combined

def fetch_readme(repo_url):
    readme_url = f"{repo_url}/raw/main/README.md"
    response = requests.get(readme_url)
    if response.status_code == 200:
        return response.text
    else:
        return "README not found."

def main():
    st.title("Background Removal and Replacement App")

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
    repo_url = "https://github.com/anurag-singh-9622/bgremover"  # Replace with your actual repo URL
    readme_content = fetch_readme(repo_url)
    st.sidebar.markdown(readme_content)

if __name__ == "__main__":
    main()