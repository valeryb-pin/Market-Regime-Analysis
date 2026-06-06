
import pandas as pd


def load_data(path):

    df = pd.read_csv(path)

    df["DateTime"] = pd.to_datetime(
        df["[Date]"].astype(str)
        + " "

        + df["[Time]"]
    )

    df = (
        df
        .set_index("DateTime")
        .sort_index()
    )

    return df
