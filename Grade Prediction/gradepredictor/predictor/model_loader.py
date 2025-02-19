import pickle
import os
from django.conf import settings

# Load the trained model
model_path = os.path.join(settings.BASE_DIR, "C:/Users/rillh/OneDrive/Desktop/Grade Prediction/linear_regression_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)
