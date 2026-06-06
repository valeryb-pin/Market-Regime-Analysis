import sys
import os
import pandas as pd

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import (
    TIMEFRAMES,
    TARGET_HORIZONS
)

from src.targets.future_returns import (
    add_future_return
)

from src.targets.breakout import (
    add_breakout_targets
)

from src.targets.target_analysis import (
    analyze_clusters
)


def run():

    print("=" * 60)
    print("TARGET ANALYSIS")
    print("=" * 60)

    os.makedirs(
        f"{PROJECT_ROOT}/results/train",
        exist_ok=True
    )

    for tf in TIMEFRAMES:

        print(f"\n{'-' * 60}")
        print(f"TIMEFRAME: {tf}")
        print(f"{'-' * 60}")

        horizon = TARGET_HORIZONS[tf]

        print(
            f"Horizon: {horizon}"
        )

        #
        # Features TRAIN
        #
        features_df = pd.read_parquet(

            f"{PROJECT_ROOT}/data/features/"
            f"{tf}_train_features.parquet"

        )

        #
        # Clusters TRAIN
        #
        clusters_df = pd.read_parquet(

            f"{PROJECT_ROOT}/data/predictions/"
            f"{tf}_train_clusters.parquet"

        )

        #
        # Crear targets futuros
        #
        features_df = add_future_return(

            features_df,

            horizon=horizon

        )

        features_df = add_breakout_targets(

            features_df,

            horizon=horizon

        )

        #
        # Mantener únicamente observaciones válidas
        #
        features_df = features_df.dropna()

        #
        # Alinear índices
        #
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

        #
        # Añadir cluster
        #
        features_df["cluster"] = (
            clusters_df["cluster"]
        )

        #
        # Análisis
        #
        summary = analyze_clusters(

            features_df,

            cluster_col="cluster"

        )

        print("\nResumen")

        print(
            summary.round(4)
        )

        #
        # Guardar
        #
        output_path = (

            f"{PROJECT_ROOT}/results/train/"
            f"{tf}_target_summary.csv"

        )

        summary.to_csv(
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
    print("TARGET ANALYSIS COMPLETADO")
    print("=" * 60)


if __name__ == "__main__":
    run()
