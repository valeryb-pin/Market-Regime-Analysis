import sys
import os
import pandas as pd

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

from src.markov.conditional_analysis import (
    create_transition_labels,
    analyze_transition_targets
)


def evaluate_split(
        timeframe,
        split,
        horizon
):

    features_df = pd.read_parquet(

        f"{PROJECT_ROOT}/data/features/"
        f"{timeframe}_{split}_features.parquet"

    )

    clusters_df = pd.read_parquet(

        f"{PROJECT_ROOT}/data/predictions/"
        f"{timeframe}_{split}_clusters.parquet"

    )

    #
    # Targets
    #
    features_df = add_future_return(
        features_df,
        horizon
    )

    features_df = add_breakout_targets(
        features_df,
        horizon
    )

    features_df = features_df.dropna()

    #
    # Alinear
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
    # Cluster
    #
    features_df["cluster"] = (
        clusters_df["cluster"]
    )

    #
    # Transition
    #
    features_df["transition"] = (

        create_transition_labels(
            features_df["cluster"]
        )

    )

    features_df = (

        features_df

        .dropna(
            subset=["transition"]
        )

    )

    #
    # Analysis
    #
    summary = (

        analyze_transition_targets(
            features_df
        )

    )

    summary = (

        summary

        .sort_values(

            ("future_return", "count"),

            ascending=False

        )

    )

    return summary
def run():

    print("=" * 60)
    print("VALIDATION OOS")
    print("=" * 60)

    os.makedirs(

        f"{PROJECT_ROOT}/results/validation",

        exist_ok=True

    )

    timeframes = [

        "1H",
        "4H"

    ]

    splits = [

        "valid",
        "oos"

    ]
    for tf in timeframes:

        print(f"\n{'='*60}")
        print(tf)
        print(f"{'='*60}")

        horizon = TARGET_HORIZONS[tf]

        for split in splits:

            print(f"\n{split.upper()}")

            summary = evaluate_split(

                tf,
                split,
                horizon

            )

            print(
                summary.head(10)
            )

            output_path = (

                f"{PROJECT_ROOT}/results/validation/"
                f"{tf}_{split}_conditional.csv"

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
    print("VALIDATION COMPLETADA")
    print("=" * 60)


if __name__ == "__main__":
    run()
