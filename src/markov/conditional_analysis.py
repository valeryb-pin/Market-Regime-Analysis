import pandas as pd


def create_transition_labels(
        clusters
):

    clusters = pd.Series(clusters)

    previous = clusters.shift(1)

    current = clusters

    transitions = (

        previous.astype("Int64")
        .astype(str)

        +

        "->"

        +

        current.astype("Int64")
        .astype(str)

    )

    return transitions
def analyze_transition_targets(
        df,
        transition_col="transition"
):

    summary = (

        df

        .groupby(transition_col)

        .agg({

            "future_return": [

                "count",

                "mean",

                "median",

                "std"

            ],

            "breakout_up": "mean",

            "breakout_down": "mean"

        })

    )

    return summary
