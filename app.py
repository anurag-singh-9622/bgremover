import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
from background_removal import remove_bg, add_bg_color, add_bg_image, add_text_behind
from utils import fetch_readme

def main():
    st.title("Background Editor App")

    tab1, tab2 = st.tabs(["Background Removal & Editing", "Add Text Behind Person"])

    with tab1:
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)

            bg_color = st.color_picker('Pick A Background Color', '#ffffff')
            st.info('Or you can upload your own background image')
            bg_image_file = st.file_uploader("Choose a background image...", type=["jpg", "png", "jpeg"])
            col1, col2 = st.columns(2)
            
            # Clear previous results when a new image is uploaded
            if 'uploaded_image' not in st.session_state or st.session_state.uploaded_image != uploaded_file:
                st.session_state.uploaded_image = uploaded_file
                st.session_state.output = None
                st.session_state.output_with_bg = None

            if 'output' not in st.session_state:
                st.session_state.output = None
            if 'output_with_bg' not in st.session_state:
                st.session_state.output_with_bg = None
            
            with col1:
                if st.button('Remove Background'):
                    st.balloons()
                    st.session_state.output = remove_bg(image)
                    
                if st.session_state.output is not None:
                    st.info("You can Right Click and Save Image on PC/ Long press and save image on mobile or download using the button below")
                    st.image(st.session_state.output, caption='Output Image.', use_column_width=True)
                    
                    buf = io.BytesIO()
                    st.session_state.output.save(buf, format="PNG")
                    st.session_state.byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="Download image without background",
                        data=st.session_state.byte_im,
                        file_name="image_without_bg.png",
                        mime="image/png"
                    )
            
            with col2:
                if st.session_state.output is not None:
                    if bg_image_file is not None:
                        bg_image = Image.open(bg_image_file)
                        st.session_state.output_with_bg = add_bg_image(st.session_state.output, bg_image)
                    else:
                        st.session_state.output_with_bg = add_bg_color(st.session_state.output, bg_color)
                    
                    st.info("You can Right Click and Save Image on PC/ Long press and save image on mobile or download using the button below")
                    st.image(st.session_state.output_with_bg, caption='Output Image with Background.', use_column_width=True)
                    
                    buf = io.BytesIO()
                    st.session_state.output_with_bg.save(buf, format="PNG")
                    st.session_state.byte_im_with_bg = buf.getvalue()
                    
                    st.download_button(
                        label="Download Image with Background",
                        data=st.session_state.byte_im_with_bg,
                        file_name="image_with_bg.png",
                        mime="image/png"
                    )

    with tab2:
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], key="text_tab")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)

            text = st.text_input("Enter text to add behind the person")
            text_position = st.text_input("Enter text position (x,y)", "10,10")
            text_color = st.color_picker('Pick A Text Color', '#000000')
            font_size = st.number_input("Font size", min_value=10, max_value=100, value=20)

            if st.button('Add Text Behind'):
                font = ImageFont.truetype("arial.ttf", font_size)
                position = tuple(map(int, text_position.split(',')))
                output_with_text = add_text_behind(image, text, position, font, text_color)
                
                st.info("You can Right Click and Save Image on PC/ Long press and save image on mobile or download using the button below")
                st.image(output_with_text, caption='Output Image with Text.', use_column_width=True)
                
                buf = io.BytesIO()
                output_with_text.save(buf, format="PNG")
                byte_im_with_text = buf.getvalue()
                
                st.download_button(
                    label="Download Image with Text",
                    data=byte_im_with_text,
                    file_name="image_with_text.png",
                    mime="image/png"
                )

    st.sidebar.title("About")
    readme_content = fetch_readme()
    st.sidebar.markdown(readme_content)

if __name__ == "__main__":
    main()