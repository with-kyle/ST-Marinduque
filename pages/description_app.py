import streamlit as st
from PIL import Image
import os

# Page title and configuration
st.set_page_config(layout="wide", page_title="Streamlit App Features Description")

# Define image paths (absolute paths assuming they are located outside the folder of this file)
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
emotion_analyzer_image_path = os.path.join(base_path, 'emotion_analyzer_image.png')
weapon_classifier_image_path = os.path.join(base_path, 'weapon_classifier_image.png')
emotion_prediction_image_path = os.path.join(base_path, 'emotion_prediction_image.png')

# Feature 1: Emotion Analyzer
st.header('Feature 1: Emotion Analyzer')
if os.path.exists(emotion_analyzer_image_path):
    emotion_analyzer_image = Image.open(emotion_analyzer_image_path)
    st.image(emotion_analyzer_image, caption='Emotion Analyzer', use_column_width=True)
else:
    st.error(f"Image not found: {emotion_analyzer_image_path}")
st.write('''
The Emotion Analyzer feature assesses emotions such as fear, anger, and joy based on textual inputs or interactions. Originally designed for analyzing sentiment from social media posts, comments, or text messages, this tool employs natural language processing (NLP) techniques to discern the underlying emotional tone. Users can input text to understand how their written communication might be perceived emotionally by others. Whether you're gauging the sentiment of online discussions, evaluating the emotional impact of marketing campaigns, or simply curious about the emotional content of text, this feature provides valuable insights into emotional expression in digital communications.
''')

# Feature 2: Image Classifier for Weapons
st.header('Feature 2: Image Classifier for Weapons')
if os.path.exists(weapon_classifier_image_path):
    weapon_classifier_image = Image.open(weapon_classifier_image_path)
    st.image(weapon_classifier_image, caption='Image Classifier for Weapons', use_column_width=True)
else:
    st.error(f"Image not found: {weapon_classifier_image_path}")
st.write('''
The Image Classifier for Weapons categorizes images based on the presence of guns, swords, or bombs. Leveraging machine learning models trained on a diverse dataset of weapon-related images, this feature allows users to upload images or use predefined examples for classification. Whether you're concerned with monitoring security risks, analyzing historical artifacts, or exploring the visual representation of weaponry in media and art, this classifier accurately identifies and categorizes images containing various types of weapons. This tool is useful for security personnel, researchers, historians, and anyone interested in the visual depiction of arms and armaments.
''')

# Feature 3: Prediction of Emotion from Internet and Social Media Interaction
st.header('Feature 3: Prediction of Emotion from Internet and Social Media Interaction')
if os.path.exists(emotion_prediction_image_path):
    emotion_prediction_image = Image.open(emotion_prediction_image_path)
    st.image(emotion_prediction_image, caption='Prediction of Emotion', use_column_width=True)
else:
    st.error(f"Image not found: {emotion_prediction_image_path}")
st.write('''
The Prediction of Emotion feature forecasts emotional responses such as happiness, sadness, excitement, and more based on user interactions across internet and social media platforms. By analyzing patterns in online behavior and communication styles, this predictive model offers insights into how digital interactions influence emotional well-being. Users can input their interaction data to receive predictions about their emotional reactions in digital environments. This feature is beneficial for understanding the emotional impact of online interactions, evaluating sentiment trends, and gaining deeper insights into personal emotional experiences online.
''')

# Footer
st.write("Explore these features to gain insights and enjoy interactive experiences with the Streamlit app!")
