import numpy as np


def add_microstructure_features(
        df,
        window=10
):

    df = df.copy()

    sign_ret = np.sign(
        df["log_return"]
    )

    df["persistence"] = (

        (
            sign_ret
            ==
            sign_ret.shift(1)

        )
        .rolling(window)
        .mean()

    )

    impact = (

        df["log_return"]
        .abs()

        /

        df["[Volume]"]
        .replace(
            0,
            np.nan
        )

    )

    df["amihud"] = (
        impact
        .rolling(window)
        .mean()
    )

    df["compression"] = (
        df["range"]
        .rolling(window)
        .std()
    )

    return df
