import pandas as pd

REQUIRED_COLS = {"Order", "Topic", "Pages"}

def validate_topics_df(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    # Clean types
    df = df.copy()

    # Order: try to make numeric for sorting
    df["Order"] = pd.to_numeric(df["Order"], errors="coerce")
    if df["Order"].isna().any():
        raise ValueError("Order column must be numeric (no blanks / text).")

    # Pages: int >= 1
    df["Pages"] = pd.to_numeric(df["Pages"], errors="coerce")
    if df["Pages"].isna().any():
        raise ValueError("Pages column must be numeric (no blanks / text).")

    df["Pages"] = df["Pages"].astype(int)
    if (df["Pages"] < 1).any():
        raise ValueError("Pages must be >= 1 for every row.")

    # Topic: non-empty
    df["Topic"] = df["Topic"].astype(str).str.strip()
    if (df["Topic"] == "").any():
        raise ValueError("Topic cannot be empty.")

    # Sort
    df = df.sort_values(by="Order", kind="stable").reset_index(drop=True)

    return df