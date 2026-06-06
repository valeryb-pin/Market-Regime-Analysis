from src.data.loader import load_data
from src.data.resampler import resample_ohlcv
from src.data.splitter import temporal_split

from config.config import *
import sys
import pandas as pd
import os


PROJECT_ROOT = "/content/drive/MyDrive/market_regime_project"

sys.path.append(PROJECT_ROOT)
def run():

    print("="*60)
    print("1. CARGANDO DATOS")
    print("="*60)

    df = load_data(
        f"{PROJECT_ROOT}/data/raw/lastoro.csv"
    )

    print("\nShape original:")
    print(df.shape)

    print("\nPrimeras filas:")
    print(df.head())

    print("\nRango temporal:")
    print(df.index.min())
    print(df.index.max())

    print("\n")
    print("="*60)
    print("2. RESAMPLE")
    print("="*60)

    datasets = {}

    for tf in TIMEFRAMES:

        datasets[tf] = resample_ohlcv(
            df,
            tf
        )

        print(
            f"{tf:10} -> "
            f"{datasets[tf].shape}"
        )

    print("\n")
    print("="*60)
    print("3. SPLIT TEMPORAL")
    print("="*60)
    print(TIMEFRAMES)

    for tf in TIMEFRAMES:

        print(f"\n------ {tf} ------")

        train, valid, oos = temporal_split(
            datasets[tf]
        )

        print("\nShapes")

        print(
            "TRAIN:",
            train.shape
        )

        print(
            "VALID:",
            valid.shape
        )

        print(
            "OOS:",
            oos.shape
        )

        print("\nFechas")

        print(
            "TRAIN:",
            train.index.min(),
            "->",
            train.index.max()
        )

        print(
            "VALID:",
            valid.index.min(),
            "->",
            valid.index.max()
        )

        print(
            "OOS:",
            oos.index.min(),
            "->",
            oos.index.max()
        )

        train_path = (
            f"{PROJECT_ROOT}/data/splits/"
            f"{tf}_train.parquet"
        )

        valid_path = (
            f"{PROJECT_ROOT}/data/splits/"
            f"{tf}_valid.parquet"
        )

        oos_path = (
            f"{PROJECT_ROOT}/data/splits/"
            f"{tf}_oos.parquet"
        )

        train.to_parquet(train_path)
        valid.to_parquet(valid_path)
        oos.to_parquet(oos_path)

        print("\nArchivos guardados")

        print(train_path)
        print(valid_path)
        print(oos_path)

    print("\n")
    print("="*60)
    print("PIPELINE FINALIZADO")
    print("="*60)


if __name__ == "__main__":
    run()
