import pandas as pd
import numpy as np


def build_transition_matrix(
        states
):

    states = pd.Series(states)

    current_state = states[:-1].values

    next_state = states[1:].values

    transitions = pd.crosstab(

        current_state,

        next_state,

        normalize="index"

    )

    return transitions
def build_transition_counts(
        states
):

    states = pd.Series(states)

    current_state = states[:-1].values

    next_state = states[1:].values

    counts = pd.crosstab(

        current_state,

        next_state

    )

    return counts
def calculate_persistence(
        transition_matrix
):

    persistence = {}

    for state in transition_matrix.index:

        persistence[state] = (

            transition_matrix
            .loc[state, state]

        )

    return pd.Series(
        persistence,
        name="persistence"
    )
