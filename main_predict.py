from pathlib import Path
from src.predict.predictor import predict_text

# if __name__ == "__main__":
#     sample_text = "Musicians to tackle US red tape  Musicians groups are to tackle US visa regulations which are blamed for hindering British acts chances of succeeding across the Atlantic.  A singer hoping to perform in the US can expect to pay $1,300 (xc2xa3680) simply for obtaining a visa. Groups including the Musicians Union are calling for an end to the ""raw deal"" faced by British performers. US acts are not faced with comparable expense and bureaucracy when visiting the UK for promotional purposes.  Nigel McCune from the Musicians Union said British musicians are ""disadvantaged"" compared to their US counterparts. A sponsor has to make a petition on their behalf, which is a form amounting to nearly 30 pages, while musicians face tougher regulations than athletes and journalists. ""If you make a mistake on your form, you risk a five-year ban and thus the ability to further your career,"" says Mr McCune.  ""The US is the worlds biggest music market, which means something has to be done about the creaky bureaucracy,"" says Mr McCune. ""The current situation is preventing British acts from maintaining momentum and developing in the US,"" he added.  The Musicians Union stance is being endorsed by the Music Managers Forum (MMF), who say British artists face ""an uphill struggle"" to succeed in the US, thanks to the tough visa requirements, which are also seen as impractical. The MMFs general secretary James Seller said: ""Imagine if you were an orchestra from the Orkneys? Every member would have to travel to London to have their visas processed.""  ""The US market is seen as the holy grail and one of the benchmarks of success, and were still going to fight to get in there. ""Its still very important, but there are other markets like Europe, India and China,"" added Mr Seller. A Department for Media, Culture and Sport spokeswoman said: ""Were aware that people are experiencing problems, and are working with the US embassy and record industry to see what we can do about it."" A US Embassy spokesman said: ""We are aware that entertainers require visas for time-specific visas and are doing everything we can to process those applications speedily."" ""We are aware of the importance of cultural exchange and we will do our best to facilitate that,"" he added. "
#     prediction = predict_text(sample_text)
#     print(f"🔥 Prediction: {prediction}")


# text_classifier/main_predict.py

# our pipeline is Pipeline([
#   ('vectorizer', CountVectorizer()),
#   ('classifier', LogisticRegression())
# ]) so it includes vectorizing + classifying 

import joblib
import pandas as pd
import argparse
from pathlib import Path

def main():
    # 1. Parse CLI args
    parser = argparse.ArgumentParser(description="Batch predict BBC categories from CSV")
    parser.add_argument("--input", required=True, help="CSV path (must have 'text' column)")
    parser.add_argument("--output", default="predictions.csv", help="Output CSV path")
    args = parser.parse_args()

    # 2. Load the complete pipeline (vectorizer + classifier)
    pipeline = joblib.load("models/logistic_regression.pkl")

    # 3. Load and predict
    df = pd.read_csv(args.input)
    df["predicted_label"] = pipeline.predict(df["text"])  # Pipeline handles all preprocessing

    # 4. Save results
    df.to_csv(args.output, index=False)
    print(f"✅ Predictions saved to {args.output}")

if __name__ == "__main__":
    main()