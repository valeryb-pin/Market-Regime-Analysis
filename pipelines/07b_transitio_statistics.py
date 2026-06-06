import sys
import os
import pandas as pd

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import (
    TIMEFRAMES
)

from src.markov.transition_matrix import (

    build_transition_matrix,

    build_transition_counts,

    calculate_persistence

)
def run():

    print("=" * 60)
    print("TRANSITION MATRIX")
    print("=" * 60)

    os.makedirs(

        f"{PROJECT_ROOT}/results/transitions",

        exist_ok=True

    )
    for tf in TIMEFRAMES:

        print(f"\n{'-'*60}")
        print(tf)
        print(f"{'-'*60}")

        clusters_df = pd.read_parquet(

            f"{PROJECT_ROOT}/data/predictions/"
            f"{tf}_train_clusters.parquet"

        )
        matrix = build_transition_matrix(

            clusters_df["cluster"]

        )

        counts = build_transition_counts(

            clusters_df["cluster"]

        )

        persistence = calculate_persistence(
            matrix
        )
        print("\nTransition Matrix")

        print(
            matrix.round(4)
        )

        print("\nPersistence")

        print(
            persistence.round(4)
        )
        matrix.to_csv(

            f"{PROJECT_ROOT}/results/transitions/"
            f"{tf}_transition_matrix.csv"

        )

        counts.to_csv(

            f"{PROJECT_ROOT}/results/transitions/"
            f"{tf}_transition_counts.csv"

        )

        persistence.to_csv(

            f"{PROJECT_ROOT}/results/transitions/"
            f"{tf}_persistence.csv"

        )
    print("\n")
    print("=" * 60)
    print("TRANSITION MATRIX COMPLETADO")
    print("=" * 60)


if __name__ == "__main__":
    run()
