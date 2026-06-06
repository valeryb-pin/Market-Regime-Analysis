import pandas as pd


def calculate_cluster_statistics(
        df,
        cluster_col="cluster"
):

    stats = (

        df
        .groupby(cluster_col)
        .agg({

            "future_return": [

                "count",
                "mean",
                "median",
                "std",
                "min",
                "max"

            ],

            "breakout_up": "mean",

            "breakout_down": "mean"

        })

    )

    return stats
