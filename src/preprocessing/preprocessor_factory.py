# Factory to build a preprocessor based on config or input
# src/preprocessing/preprocessor_factory.py
from .spacy_strategy import SpacyPreprocessor

class PreprocessorFactory:
    @staticmethod
    def get_preprocessor(name: str = "spacy"):
        if name == "spacy":
            return SpacyPreprocessor()
        else:
            raise ValueError(f"Unknown preprocessor: {name}")
