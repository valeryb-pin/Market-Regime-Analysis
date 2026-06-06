# Pipelines

This project follows a fully reproducible pipeline architecture.

## Workflow

### 01_prepare_data.py
Loads, cleans, and prepares the raw XAUUSD market data.

### 02_build_features.py
Generates market features related to:

- Order Flow
- Liquidity
- Market Efficiency
- Volatility
- Persistence
- Activity

### 03_preprocessing.py
Performs feature selection and preprocessing.

### 04_train_regimen.py
Trains the K-Means clustering model and assigns market regimes.

### 05_semantic_mapping.py
Provides semantic interpretation of the identified regimes.

### 06_target_analysis.py
Evaluates future returns and breakout targets for each regime.

### 06b_cluster_statistics.py
Computes descriptive statistics for each cluster.

### 07_build_transition_matrix.py
Builds the Markov transition matrix.

### 07b_transition_statistics.py
Computes:

- Persistence
- Expected Duration
- Transition Entropy

### 08_conditional_future_analysis.py
Evaluates future returns and breakout probabilities conditioned on regime transitions.

### 09_validation_oos.py
Performs validation and out-of-sample analysis.

### 11_visualization.py
Generates all figures and visual outputs used in the study.

## Execution Order

```bash
python pipelines/01_prepare_data.py
python pipelines/02_build_features.py
python pipelines/03_preprocessing.py
python pipelines/04_train_regimen.py
python pipelines/05_semantic_mapping.py
python pipelines/06_target_analysis.py
python pipelines/06b_cluster_statistics.py
python pipelines/07_build_transition_matrix.py
python pipelines/07b_transition_statistics.py
python pipelines/08_conditional_future_analysis.py
python pipelines/09_validation_oos.py
python pipelines/11_visualization.py
```
