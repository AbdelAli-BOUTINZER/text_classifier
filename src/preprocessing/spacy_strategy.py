# The main preprocessor using spaCy
# lowercases, removes stopwords, numbers and punctuations, and lemmatizes words
# src/preprocessing/spacy_strategy.py
import spacy
from .base_strategy import BasePreprocessor

class SpacyPreprocessor(BasePreprocessor):
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def clean(self, text: str) -> str:
        doc = self.nlp(text.lower())
        tokens = [
            token.lemma_
            for token in doc
            if not token.is_stop and not token.is_punct and not token.like_num
        ]
        return " ".join(tokens)
