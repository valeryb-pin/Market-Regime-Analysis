import pandas as pd


def build_transition_targets(df):

    data = df.copy()

    data["next_cluster"] = (
        data["cluster"]
        .shift(-1)
    )

    data = data.dropna()

    data["transition"] = (
        data["cluster"]
        .astype(str)
        + "->"
        + data["next_cluster"]
        .astype(int)
        .astype(str)
    )

    transition_stats = (

        data

        .groupby("transition")

        .agg({

            "future_return": "mean",

            "breakout_up": "mean",

            "breakout_down": "mean"

        })

        .sort_values(
            "future_return",
            ascending=False
        )

    )

    return transition_stats
