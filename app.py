import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="Object Identification", page_icon="🔍", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}  /* Hides the top-right menu */
    footer {visibility: hidden;}  /* Hides the "Made with Streamlit" footer */
    header {visibility: hidden;}  /* Hides the top Streamlit header */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def mock_api_call(file):
    return {"message": "File received", "filename": file.name}

st.title("Object Identification")

st.header("Upload an Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    response = mock_api_call(uploaded_file)
    st.write("Response:", response)

st.header("Upload a Video")
uploaded_video = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])
if uploaded_video is not None:
    st.video(uploaded_video)
    response = mock_api_call(uploaded_video)
    st.write("Response:", response)
