import sys
import os
import pandas as pd

PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)

from config.config import TIMEFRAMES

from src.features.build_features import (
    build_features
)


def run():

    print("=" * 60)
    print("BUILD FEATURES PIPELINE")
    print("=" * 60)

    os.makedirs(
        f"{PROJECT_ROOT}/data/features",
        exist_ok=True
    )

    splits = [
        "train",
        "valid",
        "oos"
    ]

    for tf in TIMEFRAMES:

        print(f"\n{'-'*50}")
        print(f"TIMEFRAME: {tf}")
        print(f"{'-'*50}")

        for split in splits:

            input_path = (
                f"{PROJECT_ROOT}/data/splits/"
                f"{tf}_{split}.parquet"
            )

            output_path = (
                f"{PROJECT_ROOT}/data/features/"
                f"{tf}_{split}_features.parquet"
            )

            print(f"\nProcesando: {tf} - {split}")

            df = pd.read_parquet(
                input_path
            )

            print(
                "Shape entrada:",
                df.shape
            )

            df_features = build_features(
                df
            )

            print(
                "Shape salida:",
                df_features.shape
            )

            df_features.to_parquet(
                output_path
            )

            print(
                f"Guardado: {output_path}"
            )

    print("\n")
    print("=" * 60)
    print("PIPELINE FINALIZADO")
    print("=" * 60)


if __name__ == "__main__":
    run()
