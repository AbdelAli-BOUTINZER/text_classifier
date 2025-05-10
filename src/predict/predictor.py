import joblib
from pathlib import Path

MODEL_PATH = Path("text_classifier/models/logistic_regression.pkl")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("❌ Trained model not found. Train it first.")
    return joblib.load(MODEL_PATH)

def predict_text(text: str) -> str:
    model = load_model()
    prediction = model.predict([text])[0]
    return prediction
