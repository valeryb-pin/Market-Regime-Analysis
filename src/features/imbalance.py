import numpy as np


def add_imbalance_features(
        df,
        window=10
):

    df = df.copy()

    total_volume = (
        df["[Volume]"]
        .rolling(window)
        .sum()
    )

    signed_volume = (
        df["signed_volume"]
        .rolling(window)
        .sum()
    )

    df["rolling_imbalance"] = (
        signed_volume
        /
        total_volume.replace(
            0,
            np.nan
        )
    )

    return df
