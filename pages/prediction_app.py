import os
import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load the model and label encoder
def load_model_and_encoder():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pkl_file_path = os.path.join(script_dir, 'prediction_mdl.pkl')
    label_encoder_path = os.path.join(script_dir, 'label_encoder.pkl')
    
    with open(pkl_file_path, 'rb') as f:
        loaded_model = pickle.load(f)
    
    with open(label_encoder_path, 'rb') as f:
        loaded_label_encoder = pickle.load(f)
    
    return loaded_model, loaded_label_encoder

# Function to predict dominant emotion
def predict_dominant_emotion(Likes_Received_Per_Day, Messages_Sent_Per_Day, Posts_Per_Day, model, label_encoder):
    input_data = pd.DataFrame({
        'Likes_Received_Per_Day': [Likes_Received_Per_Day],
        'Messages_Sent_Per_Day': [Messages_Sent_Per_Day],
        'Posts_Per_Day': [Posts_Per_Day]
    })
    
    # Ensure the columns are in the same order as the training data
    X_columns = ['Likes_Received_Per_Day', 'Messages_Sent_Per_Day', 'Posts_Per_Day']
    input_data = input_data[X_columns]
    
    # Predict the dominant emotion
    numerical_prediction = model.predict(input_data)[0]
    categorical_prediction = label_encoder.inverse_transform([int(numerical_prediction)])[0]
    
    return categorical_prediction

# Streamlit app
def main():
    st.title('Dominant Emotion Prediction App')
    
    # Load model and encoder
    model, label_encoder = load_model_and_encoder()
    
    # Input fields
    Likes_Received_Per_Day = st.number_input('Enter Likes Received Per Day:', min_value=0.0)
    Messages_Sent_Per_Day = st.number_input('Enter Messages Sent Per Day:', min_value=0.0)
    Posts_Per_Day = st.number_input('Enter Posts Per Day:', min_value=0.0)
    
    # Predict button
    if st.button('Predict Dominant Emotion'):
        result = predict_dominant_emotion(Likes_Received_Per_Day, Messages_Sent_Per_Day, Posts_Per_Day, model, label_encoder)
        st.write(f'Predicted Dominant Emotion: {result}')

if __name__ == '__main__':
    main()
