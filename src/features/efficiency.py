import numpy as np


def add_efficiency_features(
        df,
        window=10
):

    df = df.copy()

    direction = (
        df["[Close]"]
        .diff(window)
        .abs()
    )

    noise = (
        df["[Close]"]
        .diff()
        .abs()
        .rolling(window)
        .sum()
    )

    df["efficiency_ratio"] = (
        direction
        /
        noise.replace(
            0,
            np.nan
        )
    )

    return df
