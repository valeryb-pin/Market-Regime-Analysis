import numpy as np


def add_movement_features(
        df,
        vol_window=20
):

    df = df.copy()

    df["log_return"] = np.log(
        df["[Close]"]
        /
        df["[Close]"].shift(1)
    )

    df["volatility"] = (
        df["log_return"]
        .rolling(vol_window)
        .std()
    )

    df["range"] = (
        df["[High]"]
        -
        df["[Low]"]
    )

    df["range_expansion"] = (
        df["range"]
        /
        df["range"].shift(1)
    )

    return df
