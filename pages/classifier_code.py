import os
import streamlit as st

# Streamlit Web App Interface
st.set_page_config(layout="wide", page_title="Image Classification App")

st.header("Image Classifier")
st.write("This app demonstrates image classification using a trained model.")

# Displaying the code
st.header("Code")
code = """
import os
import pickle
from PIL import Image
from io import BytesIO
from img2vec_pytorch import Img2Vec
import streamlit as st

# Load the trained model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'classifier_mdl.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Initialize Img2Vec
img2vec = Img2Vec()

# Streamlit Web App Interface
st.set_page_config(layout="wide", page_title='Image Classification App')

st.write("## Image Classification Demo")
st.write(":grin: We'll try to predict the category of the uploaded image based on its features :grin:")
st.sidebar.write("## Upload an Image")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Function to convert image to bytes for display
@st.cache(suppress_st_warning=True)
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format='JPEG')
    byte_im = buf.getvalue()
    return byte_im

# Function to predict and display results
def predict_and_display(image):
    col1.write("Uploaded Image:")
    col1.image(image, use_column_width=True)

    col2.write("Prediction:")
    features = img2vec.get_vec(image)
    pred = model.predict([features])[0]
    col2.header(pred)

col1, col2 = st.columns(2)
uploaded_image = st.sidebar.file_uploader('Upload an image (PNG, JPG, JPEG)', type=['png', 'jpg', 'jpeg'])

if uploaded_image is not None:
    if uploaded_image.size > MAX_FILE_SIZE:
        st.error('Uploaded file is too large. Please upload an image smaller than 5MB.')
    else:
        image = Image.open(uploaded_image)
        predict_and_display(image)
else:
    st.write('Please upload an image to classify.')

st.write('by koalatech...')
"""
st.code(code, language='python')

# Footer
st.write("Explore image classification by uploading images and see predictions in action!")
