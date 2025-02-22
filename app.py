import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Object Identification & Live Feed")

# Section: Upload an Image
st.header("Upload an Image")
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Section: Upload a Video
st.header("Upload a Video")
uploaded_video = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])
if uploaded_video:
    st.video(uploaded_video)

# Section: Live Webcam Feed
st.header("Live Webcam Feed")

def live_feed():
    cap = cv2.VideoCapture(0)  # Open webcam (0 = default camera)
    stframe = st.empty()  # Create a placeholder for video stream

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video.")
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        img = Image.fromarray(frame)  # Convert frame to PIL Image
        stframe.image(img, caption="Live Feed", use_column_width=True)  # Display frame

    cap.release()

if st.button("Start Live Feed"):
    live_feed()
