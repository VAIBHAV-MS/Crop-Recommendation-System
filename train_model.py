import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("crop_data.csv")

# Features (inputs)
X = data.drop("label", axis=1)

# Target (output)
y = data["label"]

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# Save model
with open("crop_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Trained Successfully!")