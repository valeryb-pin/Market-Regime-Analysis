import pandas as pd
import numpy as np

def expected_duration(
        persistence
):

    duration = 1 / (1 - persistence)

    return duration


def most_likely_transition(
        matrix
):

    transitions = {}

    for state in matrix.index:

        row = matrix.loc[state].copy()

        row[state] = -1

        transitions[state] = row.idxmax()

    return pd.Series(
        transitions,
        name="most_likely_transition"
    )


def transition_entropy(
        matrix
):

    entropy = {}

    for state in matrix.index:

        probs = matrix.loc[state]

        probs = probs[probs > 0]

        ent = -(probs * np.log2(probs)).sum()

        entropy[state] = ent

    return pd.Series(
        entropy,
        name="entropy"
    )
