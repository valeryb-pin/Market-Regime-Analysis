def add_future_return(
        df,
        horizon
):

    df = df.copy()

    df["future_return"] = (

        df["[Close]"]
        .shift(-horizon)

        /

        df["[Close]"]

        - 1

    )

    return df
