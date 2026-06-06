import sys
import os
import pandas as pd

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import TIMEFRAMES

from src.preprocessing.feature_selector import (
    FEATURE_COLUMNS
)

from src.preprocessing.scaler import (
    fit_scaler,
    transform_scaler,
    save_scaler
)


def run():

    print("=" * 60)
    print("PREPROCESSING PIPELINE")
    print("=" * 60)

    splits = [
        "train",
        "valid",
        "oos"
    ]

    for tf in TIMEFRAMES:

        print(f"\n{'-'*60}")
        print(f"TIMEFRAME: {tf}")
        print(f"{'-'*60}")

        datasets = {}

        #
        # Cargar datasets
        #
        for split in splits:

            path = (
                f"{PROJECT_ROOT}/data/features/"
                f"{tf}_{split}_features.parquet"
            )

            df = pd.read_parquet(path)

            print(
                f"\n{split.upper()} antes dropna:",
                df.shape
            )

            #
            # conservar únicamente columnas
            # necesarias para clustering
            #
            df = df[FEATURE_COLUMNS]

            #
            # eliminar NaNs
            #
            df = df.dropna()

            print(
                f"{split.upper()} después dropna:",
                df.shape
            )

            datasets[split] = df

        #
        # TRAIN
        #
        train_df = datasets["train"]

        scaler = fit_scaler(
            train_df,
            FEATURE_COLUMNS
        )

        scaler_path = (
            f"{PROJECT_ROOT}/models/scaler/"
            f"{tf}_scaler.pkl"
        )

        save_scaler(
            scaler,
            scaler_path
        )

        print(
            f"\nScaler guardado: {scaler_path}"
        )

        #
        # Escalar todos los splits
        #
        for split in splits:

            scaled = transform_scaler(
                scaler,
                datasets[split],
                FEATURE_COLUMNS
            )

            scaled_df = pd.DataFrame(
                scaled,
                columns=FEATURE_COLUMNS,
                index=datasets[split].index
            )

            output_path = (
                f"{PROJECT_ROOT}/data/scaled/"
                f"{tf}_{split}_scaled.parquet"
            )

            scaled_df.to_parquet(
                output_path
            )

            print(
                f"{split.upper()} guardado:"
            )

            print(output_path)

    print("\n")
    print("=" * 60)
    print("PREPROCESSING COMPLETADO")
    print("=" * 60)


if __name__ == "__main__":
    run()
