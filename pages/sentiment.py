import streamlit as st
import pickle
import nltk
from nltk.classify import NaiveBayesClassifier
import os

# Download NLTK data
nltk.download('punkt')

# Function to extract features (words) from text
def word_features(words):
    return dict([(word, True) for word in words])

# Define emotional words and their corresponding categories
angry_words = {
  'furious', 'enraged', 'livid', 'infuriated', 'incensed', 'outraged',
  'irate', 'exasperated', 'frustrated', 'annoyed', 'irritated', 'miffed',
  'bitter', 'resentful', 'hostile', 'aggressive', 'menacing', 'threatening',
  'hateful', 'vindictive', 'malicious', 'wrathful', 'seething', 'fuming'
}

fear_words = {
  'scared', 'terrified', 'frightened', 'apprehensive', 'anxious', 'nervous',
  'worried', 'panicked', 'alarmed', 'dreadful', 'appalled', 'horrified',
  'intimidated', 'threatened', 'menacing', 'foreboding', 'ominous', 'uneasy',
  'apprehensive', 'suspicious', 'distrustful', 'paranoid', 'timid', 'cowardly',
  'frightful', 'terrifying', 'alarming', 'petrifying', 'daunting', 'formidable'
}

happy_words = {
  'happy', 'delighted', 'ecstatic', 'cheerful', 'elated', 'jubilant',
  'excited', 'grateful', 'satisfied', 'lighthearted', 'merry',
  'enjoyable', 'uplifting', 'delightful', 'fun', 'joyous',
  'charming', 'entertaining', 'positive', 'exhilarating'
}

# Combine features for training
emotions = {
    'angry': angry_words,
    'fear': fear_words,
    'happy': happy_words
}

train_set = [(word_features(word.split()), emotion) for emotion, words in emotions.items() for word in words]

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Save the trained classifier as a pickle file
current_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = os.path.join(current_dir, 'sentiment_mdl.sav')
with open(model_filename, 'wb') as model_file:
    pickle.dump(classifier, model_file)

# Function to classify emotion based on user input
def classify_emotion(input_text):
    # Load the trained classifier
    with open(model_filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    # Tokenize input text into words
    words = nltk.word_tokenize(input_text.lower())

    # Extract features from input words
    features = word_features(words)

    # Classify emotion
    emotion = loaded_model.classify(features)
    return emotion

# Streamlit app starts here
st.title("Emotion Analyzer :speech_balloon:")
message = st.text_area("Enter a sentence to analyze its emotion:")

# Function to classify sentiment and display result
def analyze_emotion():
    if message.strip():
        emotion = classify_emotion(message)
        st.write(f"Input: {message}")
        st.write(f"Predicted Emotion: {emotion}")
    else:
        st.write("Please enter a sentence to analyze.")

# Button to trigger emotion analysis
if st.button("Analyze Emotion"):
    analyze_emotion()
