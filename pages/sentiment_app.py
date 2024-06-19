import streamlit as st
import pickle
import nltk
import os

# Download NLTK data if not already downloaded
@st.cache_resource
def download_nltk_data():
    nltk.download('punkt')
download_nltk_data()

# Function to extract features (words) from text
def word_features(words):
    return dict([(word, True) for word in words])

# Function to classify emotion based on user input
def classify_emotion(input_text):
    try:
        # Tokenize input text into words
        words = nltk.word_tokenize(input_text.lower())
        # Extract features from input words
        features = word_features(words)
        # Classify emotion
        emotion = loaded_model.classify(features)
        return emotion
    except Exception as e:
        st.error(f"Error in classification: {e}")
        return None

# Determine the correct path to the model file
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'sentiment_mdl.sav')

# Load the trained Naive Bayes classifier from the saved file
if os.path.exists(model_path):
    with open(model_path, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
else:
    st.error(f"Model file {model_path} not found. Please make sure the model file is in the correct directory.")
    loaded_model = None

# Streamlit app starts here
st.title("Emotion Analyzer :speech_balloon:")
message = st.text_area("Enter a sentence to analyze its emotion:")

# Function to classify sentiment and display result
def analyze_emotion():
    if message.strip():
        if loaded_model:
            emotion = classify_emotion(message)
            if emotion:
                st.write(f"Input: {message}")
                st.write(f"Predicted Emotion: {emotion}")
        else:
            st.error("Model is not loaded. Cannot classify the text.")
    else:
        st.write("Please enter a sentence to analyze.")

# Button to trigger emotion analysis
if st.button("Analyze Emotion"):
    analyze_emotion()
