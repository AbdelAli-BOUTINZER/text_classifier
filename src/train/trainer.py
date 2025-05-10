import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import joblib
import mlflow
from mlflow.models.signature import infer_signature
from pathlib import Path

def train_model():
    # 1. Load Data - Using Path for cross-platform compatibility
    data_dir = Path("C:/Users/AbdelAli/Downloads/bbc_classification/text_classifier/data/splits")
    train_df = pd.read_csv(data_dir / "train.csv")
    test_df = pd.read_csv(data_dir / "test.csv")

    # 2. Define ML Pipeline
    pipeline = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", LogisticRegression(max_iter=200))
    ])

    X_train, y_train = train_df["clean_text"], train_df["labels"]
    X_test, y_test = test_df["clean_text"], test_df["labels"]

    # 3. MLflow Tracking
    mlflow.set_experiment("bbc_text_classification2")

    with mlflow.start_run():
        pipeline.fit(X_train, y_train)

        preds = pipeline.predict(X_test)
        acc = accuracy_score(y_test, preds)

        # Log to MLflow
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("vectorizer", "CountVectorizer")
        mlflow.log_metric("accuracy", acc)
        X_sample = pd.DataFrame(X_test[:5])
        y_sample = y_test[:5]

        signature = infer_signature(X_sample, pipeline.predict(X_sample))  

        # Save model - using Path object
        model_path = Path("text_classifier/models/logistic_regression.pkl")
        model_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(pipeline, model_path)

        # Extract and save vectorizer separately
        vectorizer = pipeline.named_steps['vectorizer']
        vectorizer_path = "text_classifier/models/vectorizer.pkl"
        joblib.dump(vectorizer, vectorizer_path)

        # Log both artifacts to MLflow
        mlflow.log_artifact(model_path)
        mlflow.log_artifact(vectorizer_path)
        
        # Log model to MLflow (better than just artifact)
        mlflow.sklearn.log_model(pipeline, "model", signature = signature, input_example = X_sample)

        

        print(f"✅ Training complete. Accuracy: {acc:.4f}")

if __name__ == "__main__":
    train_model()