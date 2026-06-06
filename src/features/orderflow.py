import numpy as np


def add_orderflow_features(df):

    df = df.copy()

    delta_close = (
        df["[Close]"]
        .diff()
    )

    df["signed_volume"] = np.where(
        delta_close > 0,
        df["[Volume]"],
        np.where(
            delta_close < 0,
            -df["[Volume]"],
            0
        )
    )

    df["cumulative_flow"] = (
        df["signed_volume"]
        .cumsum()
    )

    return df
