import cv2
import streamlit as st
import numpy as np 
from PIL import Image

def cartoonization (img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        
    value = st.sidebar.slider('Tune the brightness of your sketch (the higher the value, the brighter your sketch)', 0.0, 300.0, 250.0)
    kernel = st.sidebar.slider('Tune the boldness of the edges of your sketch (the higher the value, the bolder the edges)', 1, 99, 25, step=2)


    gray_blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)

    cartoon = cv2.divide(gray, gray_blur, scale=value)
    return cartoon


st.write("""
          # Cartoonize Your Image!
          """
          )

st.write("This is an app to turn your photos into cartoon")

file = st.sidebar.file_uploader("Please upload an image file", type=["jpg", "png","jpeg"])

if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    img = np.array(image)

    st.text("Your original image")
    st.image(img, use_column_width=True)
    
    st.text("Your cartoonized image")
    cartoon = cartoonization(img)
    
    st.image(cartoon, use_column_width=True)

