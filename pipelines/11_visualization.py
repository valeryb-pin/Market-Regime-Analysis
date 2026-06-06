import sys
import os

import pandas as pd
import numpy as np

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import TARGET_HORIZONS

from src.targets.future_returns import add_future_return
from src.targets.breakout import add_breakout_targets

from src.visualization.regime_plots import (
    plot_cluster_distribution,
    plot_cluster_returns,
    plot_transition_matrix,
    plot_persistence_analysis,
    plot_regime_timeline,
    plot_cluster_targets,
    plot_transition_statistics,
    plot_regime_stability,
    plot_transition_network,
    plot_transition_target_heatmap,
    plot_transition_validation_oos
)

from src.targets.transition_analysis import (
    build_transition_targets
)

def run():

    print("=" * 60)
    print("VISUALIZATION")
    print("=" * 60)

    timeframes = ["1H", "4H"]

    os.makedirs(
    f"{PROJECT_ROOT}/results/figures",
    exist_ok=True
    )


    for tf in ["1H","4H"]:

        valid_df = pd.read_csv(
            f"{PROJECT_ROOT}/results/validation/"
            f"{tf}_valid_conditional.csv",
            header=[0,1],
            index_col=0
        )

        oos_df = pd.read_csv(
            f"{PROJECT_ROOT}/results/validation/"
            f"{tf}_oos_conditional.csv",
            header=[0,1],
            index_col=0
        )

        print(f"\n{'-'*60}")
        print(tf)
        print(f"{'-'*60}")

        horizon = TARGET_HORIZONS[tf]

        features_df = pd.read_parquet(
            f"{PROJECT_ROOT}/data/features/{tf}_train_features.parquet"
        )

        clusters_df = pd.read_parquet(
            f"{PROJECT_ROOT}/data/predictions/{tf}_train_clusters.parquet"
        )

        features_df = add_future_return(
            features_df,
            horizon=horizon
        )

        features_df = add_breakout_targets(
            features_df,
            horizon=horizon
        )

        common_index = (
            features_df.index
            .intersection(clusters_df.index)
        )

        features_df = features_df.loc[common_index]
        clusters_df = clusters_df.loc[common_index]

        features_df["cluster"] = clusters_df["cluster"]
        
        transition_targets = (
            build_transition_targets(
                features_df
            )
        )

        output_dir = (
            f"{PROJECT_ROOT}/results/figures/{tf}"
        )

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        plot_cluster_distribution(
            features_df,
            output_dir
        )

        plot_cluster_returns(
            features_df,
            output_dir
        )

        plot_transition_matrix(
            features_df,
            output_dir
        )

        plot_persistence_analysis(
            features_df,
            output_dir
        )

        # Timeline requiere precio
        ohlc_df = pd.read_parquet(
          f"{PROJECT_ROOT}/data/splits/{tf}_train.parquet"
        )

        common_index = (
            ohlc_df.index
            .intersection(features_df.index)
        )

        timeline_df = ohlc_df.loc[common_index].copy()

        timeline_df["cluster"] = (
            features_df.loc[common_index, "cluster"]
        )

        plot_regime_timeline(
            timeline_df,
            output_dir
        )

        print(
            f"Figuras guardadas en: {output_dir}"
        )

        stats = pd.read_csv(
           f"{PROJECT_ROOT}/results/statistics/"
           f"{tf}_cluster_statistics.csv",
           header=[0,1],
           index_col=0
        )

        print("\nColumns:")
        print(stats.columns)

        plot_cluster_targets(
          stats,
          tf,
          output_dir
        )
        
        transition_stats = pd.read_csv(
             f"{PROJECT_ROOT}/results/"
             f"transition_statistics/"
             f"{tf}_transition_statistics.csv",
             index_col=0
        )
    
    
        transition_matrix = pd.read_csv(
            f"{PROJECT_ROOT}/results/transitions/"
            f"{tf}_transition_matrix.csv",
            index_col=0
        )
        
        transition_matrix.columns = (
            transition_matrix.columns.astype(int)
        )
        print("\nTransition Matrix")
        print(transition_matrix)
        
        plot_transition_statistics(
            transition_stats,
            tf,
            output_dir
        )
        
        plot_transition_network(
            transition_matrix,
            transition_stats,
            tf,
            output_dir
        )
        
        plot_transition_target_heatmap(
            transition_targets,
            tf,
            output_dir
        )
        
        
        # ----------------------------------
# VALID vs OOS
# ----------------------------------

        valid_df = pd.read_csv(
            f"{PROJECT_ROOT}/results/validation/"
            f"{tf}_valid_conditional.csv",
            header=[0,1],
            index_col=0
        )

        oos_df = pd.read_csv(
            f"{PROJECT_ROOT}/results/validation/"
            f"{tf}_oos_conditional.csv",
            header=[0,1],
            index_col=0
        )

        common_transitions = (
            valid_df.index
            .intersection(oos_df.index)
        )

        comparison_df = pd.DataFrame({

            "VALID":
                valid_df.loc[
                    common_transitions,
                    ("future_return","mean")
                ],

            "OOS":
                oos_df.loc[
                    common_transitions,
                    ("future_return","mean")
                ]

        })

        comparison_df = (
            comparison_df
            .sort_values(
                "OOS",
                ascending=False
            )
            .head(8)
        )

        plot_transition_validation_oos(
            comparison_df,
            tf,
            output_dir
        )

        print("ENTRANDO A plot_regime_stability")
        print(stats.head())
        print(output_dir)
        
        plot_regime_stability(
            transition_stats,
            tf,
            output_dir)

    print("=" * 60)
    print("VISUALIZATION COMPLETADO")
    print("=" * 60)



if __name__ == "__main__":
    run()
