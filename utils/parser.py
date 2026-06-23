# utils/parser.py

import pandas as pd


VALID_SLOTS = ["Morning", "PrimeTime", "Evening"]


def parse_uploaded_file(uploaded_file):
    """
    Reads uploaded txt file and converts into dataframe
    """

    try:
        df = pd.read_csv(
            uploaded_file,
            header=None,
            names=[
                "Ad_ID",
                "Duration",
                "Budget",
                "Priority",
                "Preferred_Slot"
            ]
        )

        validate_dataset(df)

        return df

    except Exception as e:
        raise Exception(f"Error parsing file: {e}")


def validate_dataset(df):
    """
    Validates dataset
    """

    required_cols = [
        "Ad_ID",
        "Duration",
        "Budget",
        "Priority",
        "Preferred_Slot"
    ]

    for col in required_cols:
        if col not in df.columns:
            raise Exception("Invalid dataset format")

    for slot in df["Preferred_Slot"]:
        if slot not in VALID_SLOTS:
            raise Exception(
                f"Invalid slot detected: {slot}"
            )

    if (df["Duration"] <= 0).any():
        raise Exception(
            "Duration cannot be negative"
        )

    if (df["Budget"] <= 0).any():
        raise Exception(
            "Budget cannot be negative"
        )

    if ((df["Priority"] < 1) |
        (df["Priority"] > 10)).any():

        raise Exception(
            "Priority must be between 1 and 10"
        )


def dataframe_to_ads(df):
    """
    Converts dataframe into list of dictionaries
    """

    ads = []

    for _, row in df.iterrows():

        ads.append({

            "id": row["Ad_ID"],
            "duration": int(row["Duration"]),
            "budget": int(row["Budget"]),
            "priority": int(row["Priority"]),
            "slot": row["Preferred_Slot"]

        })

    return ads