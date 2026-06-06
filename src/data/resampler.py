
def resample_ohlcv(df, timeframe):

    return (
        df[
            [
                "[Open]",
                "[High]",
                "[Low]",
                "[Close]",
                "[Volume]"
            ]
        ]
        .resample(timeframe)
        .agg({
            "[Open]": "first",
            "[High]": "max",
            "[Low]": "min",
            "[Close]": "last",
            "[Volume]": "sum"
        })
        .dropna()
    )
