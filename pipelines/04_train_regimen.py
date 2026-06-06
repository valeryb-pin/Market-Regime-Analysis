import sys
import os
import pandas as pd

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import (
    TIMEFRAMES,
    N_CLUSTERS,
    SEED
)

from src.clustering.train import (
    fit_kmeans
)

from src.clustering.inference import (
    predict_clusters
)

from src.clustering.persistence import (
    save_model
)
def run():

    print("="*60)
    print("TRAIN REGIMES")
    print("="*60)

    os.makedirs(
        f"{PROJECT_ROOT}/data/predictions",
        exist_ok=True
    )

    os.makedirs(
        f"{PROJECT_ROOT}/models/kmeans",
        exist_ok=True
    )
    for tf in TIMEFRAMES:
        print(f"\n{'-'*60}")
        print(tf)
        print(f"{'-'*60}")

        train_df = pd.read_parquet(

            f"{PROJECT_ROOT}/data/scaled/"
            f"{tf}_train_scaled.parquet"

        )

        valid_df = pd.read_parquet(

            f"{PROJECT_ROOT}/data/scaled/"
            f"{tf}_valid_scaled.parquet"

        )

        oos_df = pd.read_parquet(

            f"{PROJECT_ROOT}/data/scaled/"
            f"{tf}_oos_scaled.parquet"

        )

        model = fit_kmeans(
            train_df,
            n_clusters=N_CLUSTERS,
            random_state=SEED
        )

        model_path = (
            f"{PROJECT_ROOT}/models/kmeans/"
            f"{tf}_kmeans.pkl"
        )

        save_model(
            model,
            model_path
        )

        train_clusters = predict_clusters(
            model,
            train_df
        )

        valid_clusters = predict_clusters(
            model,
            valid_df
        )

        oos_clusters = predict_clusters(
            model,
            oos_df
        )
        train_pred = pd.DataFrame(index=train_df.index)
        train_pred["cluster"] = train_clusters
        train_pred.to_parquet(

            f"{PROJECT_ROOT}/data/predictions/"
            f"{tf}_train_clusters.parquet"
        )

        print(
        f"{tf} completado"
        )

        print(
        f"Modelo: {model_path}"
        )

        valid_pred = pd.DataFrame(index=valid_df.index)
        valid_pred["cluster"] = valid_clusters
        valid_pred.to_parquet(

            f"{PROJECT_ROOT}/data/predictions/"
            f"{tf}_valid_clusters.parquet"
        )
        print(
        f"{tf} completado"
        )

        print(
        f"Modelo: {model_path}"
        )

        oos_pred = pd.DataFrame(index=oos_df.index)
        oos_pred["cluster"] = oos_clusters
        oos_pred.to_parquet(

            f"{PROJECT_ROOT}/data/predictions/"
            f"{tf}_oos_clusters.parquet"

        )
        print(
        f"{tf} completado"
        )

        print(
        f"Modelo guardado: {model_path}"
        )

        print("\nDistribución clusters TRAIN")

        print(
        pd.Series(train_clusters)
        .value_counts()
        .sort_index()
        )

import seaborn as sns
import matplotlib.pyplot as plt

cluster_profiles = (
    df
    .groupby("cluster")[
        feature_cols
    ]
    .mean()
)

plt.figure(figsize=(12,6))

sns.heatmap(
    cluster_profiles,
    cmap="RdYlGn",
    center=0,
    annot=True,
    fmt=".2f"
)

plt.title("Perfil Estandarizado de los Regímenes")
plt.ylabel("Cluster")
plt.xlabel("Variables")

plt.show()

if __name__ == "__main__":
    run()
