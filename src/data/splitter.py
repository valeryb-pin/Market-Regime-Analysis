
def temporal_split(
        df,
        train_pct=0.60,
        valid_pct=0.20
):

    n = len(df)

    train_end = int(
        n * train_pct
    )

    valid_end = int(
        n * (
            train_pct
            + valid_pct
        )
    )

    train = df.iloc[:train_end]

    valid = df.iloc[
        train_end:valid_end
    ]

    oos = df.iloc[
        valid_end:
    ]

    return train, valid, oos
