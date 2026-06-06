from sklearn.cluster import KMeans


def fit_kmeans(
        X,
        n_clusters,
        random_state=42
):

    model = KMeans(

        n_clusters=n_clusters,

        random_state=random_state,

        n_init=20

    )

    model.fit(X)

    return model
