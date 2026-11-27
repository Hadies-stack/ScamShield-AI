
from pathlib import Path

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_DIR / "data" / "SMSSpamCollection"
MODEL_PATH = PROJECT_DIR / "data" / "sms_spam_model.joblib"


def train_model():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    data = pd.read_csv(
        DATASET_PATH,
        sep="\t",
        header=None,
        names=["label", "message"],
    )

    data = data.dropna()
    data = data[data["label"].isin(["ham", "spam"])]

    X = data["message"].astype(str)
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),
                min_df=1,
                sublinear_tf=True,
            ),
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ])

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    metrics = {
        "accuracy": round(accuracy_score(y_test, predictions) * 100, 2),
        "precision": round(
            precision_score(y_test, predictions, pos_label="spam") * 100, 2
        ),
        "recall": round(
            recall_score(y_test, predictions, pos_label="spam") * 100, 2
        ),
        "f1_score": round(
            f1_score(y_test, predictions, pos_label="spam") * 100, 2
        ),
    }

    # Train final model on the complete dataset.
    model.fit(X, y)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return {
        "records": len(data),
        "ham": int((y == "ham").sum()),
        "spam": int((y == "spam").sum()),
        "metrics": metrics,
        "model_path": str(MODEL_PATH),
    }


def predict_sms(message):
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "SMS model not trained yet. Run train_model() first."
        )

    if not message or not message.strip():
        raise ValueError("Please enter an SMS message.")

    model = joblib.load(MODEL_PATH)

    probabilities = model.predict_proba([message])[0]
    classes = list(model.classes_)

    spam_probability = float(
        probabilities[classes.index("spam")] * 100
    )

    prediction = model.predict([message])[0]

    return {
        "prediction": prediction,
        "spam_probability": round(spam_probability, 2),
        "label": (
            "Spam-like message"
            if prediction == "spam"
            else "Likely legitimate message"
        ),
        "disclaimer": (
            "This model estimates SMS spam likelihood. "
            "It does not confirm fraud or prove a message is safe."
        ),
    }
