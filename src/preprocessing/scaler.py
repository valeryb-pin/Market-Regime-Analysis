import joblib

from sklearn.preprocessing import (
    StandardScaler
)

def fit_scaler(
        df,
        feature_cols
):

    scaler = StandardScaler()

    scaler.fit(
        df[feature_cols]
    )

    return scaler


def transform_scaler(
        scaler,
        df,
        feature_cols
):

    return scaler.transform(
        df[feature_cols]
    )


def save_scaler(
        scaler,
        path
):

    joblib.dump(
        scaler,
        path
    )


def load_scaler(path):

    return joblib.load(path)
