
import sys
import pandas as pd

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import (
    TIMEFRAMES
)

from src.preprocessing.feature_selector import (
    FEATURE_COLUMNS
)

from src.semantic.mapping import (
    build_cluster_profile,
    rank_clusters
)

from src.semantic.visualization import (
    plot_regime_profiles,
    plot_regime_bars
)


def run():

    print("=" * 60)
    print("SEMANTIC MAPPING")
    print("=" * 60)

    for tf in TIMEFRAMES:

        print(f"\n{'-' * 60}")
        print(tf)
        print(f"{'-' * 60}")

        features_df = pd.read_parquet(
            f"{PROJECT_ROOT}/data/features/"
            f"{tf}_train_features.parquet"
        )

        features_df = (
            features_df
            [FEATURE_COLUMNS]
            .dropna()
        )

        clusters_df = pd.read_parquet(
            f"{PROJECT_ROOT}/data/predictions/"
            f"{tf}_train_clusters.parquet"
        )

        profile = build_cluster_profile(
            features_df,
            clusters_df
        )

        print("\nPerfil")
        print(
            profile.round(3)
        )

        # Generar heatmap
        plot_regime_profiles(
            profile,
            tf,
            save_path=(
                f"{PROJECT_ROOT}/results/figures/"
                f"{tf}_regime_profiles.png"
            )
        )
        plot_regime_bars(
          profile,
          tf,
          save_path=(
            f"{PROJECT_ROOT}/results/figures/"
            f"{tf}_regime_bars.png"
          )
        )

        ranking = rank_clusters(
            profile
        )

        print("\nRanking")
        print(ranking)

        profile.to_csv(
            f"{PROJECT_ROOT}/models/mappings/"
            f"{tf}_cluster_profile.csv"
        )

        ranking.to_csv(
            f"{PROJECT_ROOT}/models/mappings/"
            f"{tf}_cluster_ranking.csv"
        )


if __name__ == "__main__":
    run()
