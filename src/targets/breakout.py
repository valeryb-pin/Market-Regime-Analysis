import numpy as np


def add_breakout_targets(
        df,
        horizon=5,
        threshold=0.01
):

    df = df.copy()

    future_max = (

        df["[High]"]
        .rolling(horizon)
        .max()
        .shift(-horizon)

    )

    future_min = (

        df["[Low]"]
        .rolling(horizon)
        .min()
        .shift(-horizon)

    )

    df["breakout_up"] = (

        (
            future_max
            /
            df["[Close]"]
            - 1
        )
        >
        threshold

    ).astype(int)

    df["breakout_down"] = (

        (
            future_min
            /
            df["[Close]"]
            - 1
        )
        <
        -threshold

    ).astype(int)

    return df
