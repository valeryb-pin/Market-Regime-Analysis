import sys
import os
import pandas as pd
import numpy as np

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import (
    TARGET_HORIZONS
)

from src.targets.future_returns import (
    add_future_return
)

from src.targets.breakout import (
    add_breakout_targets
)

from src.targets.cluster_statistics import (
    calculate_cluster_statistics
)
def run():

    print("=" * 60)
    print("CLUSTER STATISTICS")
    print("=" * 60)

    os.makedirs(

        f"{PROJECT_ROOT}/results/statistics",

        exist_ok=True

    )

    timeframes = [

        "1H",

        "4H"

    ]
    for tf in timeframes:
        print(f"\n{'-'*60}")
        print(tf)
        print(f"{'-'*60}")

        horizon = TARGET_HORIZONS[tf]
        features_df = pd.read_parquet(
            f"{PROJECT_ROOT}/data/features/"
            f"{tf}_train_features.parquet"
        )

        clusters_df = pd.read_parquet(

            f"{PROJECT_ROOT}/data/predictions/"
            f"{tf}_train_clusters.parquet"

        )
        features_df = add_future_return(
            features_df,
            horizon=horizon
        )

        features_df = add_breakout_targets(
            features_df,
            horizon=horizon
        )

        features_df = features_df.dropna()

        common_index = (

            features_df.index

            .intersection(

                clusters_df.index

            )

        )

        features_df = (

            features_df
            .loc[common_index]

        )

        clusters_df = (

            clusters_df
            .loc[common_index]

        )

        features_df["cluster"] = (

            clusters_df["cluster"]

        )

        sharpe_like = (

            features_df

            .groupby("cluster")

            ["future_return"]

            .mean()

            /

            features_df

            .groupby("cluster")

            ["future_return"]

            .std()

        )

        stats[("future_return","sharpe_like")] = (

            sharpe_like

        )
        stats = stats.round(6)
        print("\n")
        print(stats)

        output_path = (

            f"{PROJECT_ROOT}/results/statistics/"
            f"{tf}_cluster_statistics.csv"

        )

        stats.to_csv(
            output_path
        )

        print(

            f"\nGuardado:"

        )

        print(
            output_path
        )

        print("\n")
        print("=" * 60)
        print("CLUSTER STATISTICS COMPLETADO")
        print("=" * 60)
        print(stats.columns)


if __name__ == "__main__":
    run()
