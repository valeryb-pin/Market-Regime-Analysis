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
def run():

    print("="*60)
    print("CONDITIONAL FUTURE ANALYSIS")
    print("="*60)

    os.makedirs(

        f"{PROJECT_ROOT}/results/conditional",

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
        summary = (

            analyze_transition_targets(

                features_df

            )

        )
        summary = (

            summary

            .sort_values(

                ("future_return","count"),

                ascending=False

            )

        )
        print("\nTop Transition Analysis")

        print(

            summary.head(10)

        )
        output_path = (

            f"{PROJECT_ROOT}/results/conditional/"
            f"{tf}_conditional_analysis.csv"

        )

        summary.to_csv(
            output_path
        )

        print(
            f"\nGuardado:"
        )

        print(output_path)
    print("\n")
    print("="*60)
    print("CONDITIONAL ANALYSIS COMPLETADO")
    print("="*60)


if __name__ == "__main__":
    run()
