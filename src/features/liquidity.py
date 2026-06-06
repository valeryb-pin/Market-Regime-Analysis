import numpy as np
def add_liquidity_features(df):

    df = df.copy()

    spread = (
        df["[High]"]
        -
        df["[Low]"]
    )

    df["spread_proxy"] = spread

    df["volume_range_ratio"] = (
        df["[Volume]"]
        /
        spread.replace(
            0,
            np.nan
        )
    )

    return df
