# Methodology

## Data Preparation

Historical XAUUSD data was collected and resampled into multiple timeframes.

## Feature Engineering

Features were generated across several dimensions:

- Market Efficiency
- Liquidity
- Volatility
- Persistence
- Activity
- Order Flow

## Feature Selection

A subset of features was selected for clustering.

Selected Features:

- rolling_imbalance
- efficiency_ratio
- compression
- amihud
- persistence
- volume_range_ratio
- volatility

## Regime Identification

K-Means clustering was used to identify recurring market states.

## Regime Characterization

Clusters were analyzed through their feature profiles.

## Target Analysis

The following targets were evaluated:

- Future Return
- Breakout Up
- Breakout Down

## Markov Analysis

Transition matrices were estimated to study regime evolution.

Metrics:

- Persistence
- Expected Duration
- Entropy

## Transition Analysis

Targets were evaluated conditional on regime transitions.

## Validation

Transition behavior was tested on validation and out-of-sample datasets.
