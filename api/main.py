from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import spacy

# Load NLP
nlp = spacy.load("en_core_web_sm")

# Load pipeline (vectorizer + classifier)
model = joblib.load("text_classifier/models/logistic_regression.pkl")

# Init FastAPI app
app = FastAPI(title="BBC Text Classifier API")

# Request body format
class TextRequest(BaseModel):
    text: str

# Preprocess text
def preprocess(text: str) -> str:
    doc = nlp(text)
    tokens = [
        token.lemma_.lower() for token in doc
        if not token.is_stop and not token.is_punct and token.is_alpha
    ]
    return " ".join(tokens)

# Root endpoint
@app.get("/")
def root():
    return {"message": "🔥 BBC Text Classifier is ready 🔥"}

# Predict endpoint
@app.post("/predict")
def predict(request: TextRequest):
    try:
        clean_text = preprocess(request.text)
        prediction = model.predict([clean_text])[0]
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
