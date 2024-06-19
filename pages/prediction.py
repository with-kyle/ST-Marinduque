import os
import pandas as pd
from ydata_profiling import ProfileReport  # Updated import
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import pickle

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define file paths
csv_file_path = os.path.join(script_dir, 'test.csv')
pkl_file_path = os.path.join(script_dir, 'prediction_mdl.pkl')

# Print current working directory and files in the script directory
print("Current Working Directory:", os.getcwd())
print("Files in the script directory:", os.listdir(script_dir))

# Check if the CSV file exists
if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"The file {csv_file_path} does not exist.")

# Load the dataset
datasetCSV = pd.read_csv(csv_file_path)

# Display the head of the dataset
print(datasetCSV.head())

# Preprocess the data
# Selecting relevant columns and dropping rows with missing values
datasetCSV = datasetCSV[['Likes_Received_Per_Day', 'Messages_Sent_Per_Day', 'Posts_Per_Day', 'Dominant_Emotion']]
datasetCSV = datasetCSV.dropna()

# Encode the target variable
label_encoder = LabelEncoder()
datasetCSV['Dominant_Emotion'] = label_encoder.fit_transform(datasetCSV['Dominant_Emotion'])

# Define the features (X) and the target (y)
X = datasetCSV.drop('Dominant_Emotion', axis=1)
y = datasetCSV['Dominant_Emotion']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')

# Save the model to a pickle file
with open(pkl_file_path, 'wb') as f:
    pickle.dump(model, f)

# Save the label encoder to a pickle file
label_encoder_path = os.path.join(script_dir, 'label_encoder.pkl')
with open(label_encoder_path, 'wb') as f:
    pickle.dump(label_encoder, f)

# Load the model from the pickle file
with open(pkl_file_path, 'rb') as f:
    loaded_model = pickle.load(f)

# Load the label encoder from the pickle file
with open(label_encoder_path, 'rb') as f:
    loaded_label_encoder = pickle.load(f)

# Function to predict dominant emotion
def predict_dominant_emotion(Likes_Received_Per_Day, Messages_Sent_Per_Day, Posts_Per_Day):
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'Likes_Received_Per_Day': [Likes_Received_Per_Day],
        'Messages_Sent_Per_Day': [Messages_Sent_Per_Day],
        'Posts_Per_Day': [Posts_Per_Day]
    })

    # Add missing columns with zeros
    for col in X.columns:
        if col not in input_data.columns:
            input_data[col] = 0

    # Ensure the columns are in the same order as the training data
    input_data = input_data[X.columns]

    # Predict the dominant emotion
    numerical_prediction = loaded_model.predict(input_data)[0]
    
    # Decode the numerical prediction back to the categorical label
    categorical_prediction = loaded_label_encoder.inverse_transform([int(numerical_prediction)])[0]
    
    return categorical_prediction

# Example prediction
example_Likes_Received_Per_Day = 30
example_Messages_Sent_Per_Day = 15
example_Posts_Per_Day = 5
predicted_Dominant_Emotion = predict_dominant_emotion(example_Likes_Received_Per_Day, example_Messages_Sent_Per_Day, example_Posts_Per_Day)
print(f'Predicted Dominant Emotion: {predicted_Dominant_Emotion}')
