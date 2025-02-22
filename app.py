import streamlit as st
import cv2
import numpy as np
from PIL import Image

def mock_api_call(file):
    return {"message": "File received", "filename": file.name}

st.title("Object Identification")

# --- IMAGE UPLOAD SECTION ---
st.header("Upload an Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    response = mock_api_call(uploaded_file)
    st.write("Response:", response)

# --- VIDEO UPLOAD SECTION ---
st.header("Upload a Video")
uploaded_video = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])
if uploaded_video is not None:
    st.video(uploaded_video)
    response = mock_api_call(uploaded_video)
    st.write("Response:", response)

# --- LIVE FEED SECTION ---
st.header("Live Camera Feed")

# Start the webcam
video_capture = cv2.VideoCapture(0)  # 0 for default webcam

# Create a Streamlit empty container for the feed
live_feed = st.empty()

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        st.warning("Webcam not accessible.")
        break
    
    # Convert frame to RGB (OpenCV uses BGR by default)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Display the live feed
    live_feed.image(frame, channels="RGB", use_column_width=True)
    
    # Stop the loop when user closes the app
    if st.button("Stop Live Feed"):
        break

video_capture.release()
cv2.destroyAllWindows()
