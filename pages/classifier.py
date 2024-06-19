import os
import pickle

from img2vec_pytorch import Img2Vec
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Initialize Img2Vec
img2vec = Img2Vec()

# Prepare data
current_dir = os.path.dirname(os.path.abspath(__file__))
# dataset directory is a sibling of the pages directory
data_dir = os.path.join(current_dir, '..', 'dataset')
train_dir = os.path.join(data_dir, 'train')
val_dir = os.path.join(data_dir, 'val')

# Check if the directories exist
if not os.path.exists(train_dir):
    raise FileNotFoundError(f"Training directory not found: {train_dir}")
if not os.path.exists(val_dir):
    raise FileNotFoundError(f"Validation directory not found: {val_dir}")

data = {}
for j, dir_ in enumerate([train_dir, val_dir]):
    features = []
    labels = []
    for category in os.listdir(dir_):
        category_dir = os.path.join(dir_, category)
        if os.path.isdir(category_dir):
            for img_path in os.listdir(category_dir):
                img_path_ = os.path.join(category_dir, img_path)
                if os.path.isfile(img_path_):
                    img = Image.open(img_path_).convert('RGB')
                    img_features = img2vec.get_vec(img)
                    features.append(img_features)
                    labels.append(category)
    if j == 0:
        data['training_data'] = features
        data['training_labels'] = labels
    else:
        data['validation_data'] = features
        data['validation_labels'] = labels

# Train model
model = RandomForestClassifier(random_state=0)
model.fit(data['training_data'], data['training_labels'])

# Test performance
y_pred = model.predict(data['validation_data'])
score = accuracy_score(y_pred, data['validation_labels'])

print(f"Validation Accuracy: {score:.4f}")

# Save the model
model_path = os.path.join(current_dir, 'classifier_mdl.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved as '{model_path}'")
