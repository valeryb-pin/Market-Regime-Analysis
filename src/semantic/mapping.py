import pandas as pd


def build_cluster_profile(
        features_df,
        clusters_df
):

    df = features_df.copy()

    df["cluster"] = (
        clusters_df["cluster"]
    )

    profile = (

        df
        .groupby("cluster")
        .mean()

    )

    return profile

def rank_clusters(profile):

    ranked = profile.rank(
        ascending=False
    )

    return ranked
