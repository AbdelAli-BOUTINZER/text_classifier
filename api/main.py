from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import joblib
import spacy
from prometheus_fastapi_instrumentator import Instrumentator

# 🔐 Security + 🔍 Logger
from .security import verify_token
from .logger import log_to_file




# Load NLP
nlp = spacy.load("en_core_web_sm")

# Load model
model = joblib.load("text_classifier/models/logistic_regression.pkl")

# FastAPI app
app = FastAPI(title="BBC Text Classifier API")

# 📊 Monitoring
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

class TextRequest(BaseModel):
    text: str

# 🔍 Log preprocessing
@log_to_file
def preprocess(text: str) -> str:
    doc = nlp(text)
    tokens = [
        token.lemma_.lower() for token in doc
        if not token.is_stop and not token.is_punct and token.is_alpha
    ]
    return " ".join(tokens)

@app.get("/")
@log_to_file
def root():
    return {"message": " News article Text Classifier is ready (adnane-abdelali-abdelahy) ⚠🚸☢☢🛐🕉"}

@app.post("/predict")
@log_to_file
def predict(request: TextRequest, _: str = Depends(verify_token)):
    try:
        clean_text = preprocess(request.text)
        prediction = model.predict([clean_text])[0]
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


