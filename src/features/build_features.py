from src.features.movement import (
    add_movement_features
)

from src.features.liquidity import (
    add_liquidity_features
)

from src.features.orderflow import (
    add_orderflow_features
)

from src.features.imbalance import (
    add_imbalance_features
)

from src.features.efficiency import (
    add_efficiency_features
)

from src.features.microstructure import (
    add_microstructure_features
)


def build_features(df):

    df = add_movement_features(df)

    df = add_liquidity_features(df)

    df = add_orderflow_features(df)

    df = add_imbalance_features(df)

    df = add_efficiency_features(df)

    df = add_microstructure_features(df)

    return df
