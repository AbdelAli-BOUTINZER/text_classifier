# abstract class for all preprocessors

# src/preprocessing/base_strategy.py
from abc import ABC, abstractmethod

class BasePreprocessor(ABC):
    @abstractmethod
    def clean(self, text: str) -> str:
        pass
