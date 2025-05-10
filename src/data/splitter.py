from pathlib import Path
from typing import Optional
import pandas as pd
from sklearn.model_selection import train_test_split
from pydantic import BaseModel, field_validator


class SplitConfig(BaseModel):
    input_file: Path
    train_file: Path
    test_file: Path
    test_size: float = 0.2
    random_state: int = 0

    @field_validator('test_size')
    def test_size_range(cls, v):
        if not 0 < v < 1:
            raise ValueError("test_size must be between 0 and 1")
        return v


def split_data(config: SplitConfig):
    print("📂 Loading dataset...")
    df = pd.read_csv(config.input_file)

    print(f"🔀 Splitting data (test size = {config.test_size})...")
    train_df, test_df = train_test_split(
        df,
        test_size=config.test_size,
        random_state=config.random_state,
        stratify=df['category'] if 'category' in df.columns else None
    )

    print(f"💾 Saving training data to {config.train_file}")
    train_df.to_csv(config.train_file, index=False)

    print(f"💾 Saving test data to {config.test_file}")
    test_df.to_csv(config.test_file, index=False)

    print("✅ Data split completed successfully.")


if __name__ == "__main__": # This is a script to run the splitter directly
    config = SplitConfig(
    input_file=Path("data/processed/bbc_clean.csv"),  # ⬅️ updated path
    train_file=Path("data/splits/train.csv"),
    test_file=Path("data/splits/test.csv"),
    test_size=0.2,
    random_state=0
)

    split_data(config)