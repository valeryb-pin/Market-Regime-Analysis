## Overview

Financial markets are often described as chaotic and unpredictable systems. However, recurring market structures may emerge when behavior is analyzed through data.

This project investigates whether financial markets can be represented as a sequence of observable regimes rather than a purely random process. Using clustering techniques and Markov chains, the study identifies market states, characterizes their behavior, and analyzes how transitions between regimes influence future market outcomes.

The analysis is performed on XAUUSD (Gold Spot) data and focuses on regime persistence, transition dynamics, and directional market behavior.

---

## Research motivation

One of the central challenges in financial markets is distinguishing between randomness and structure.

If markets are completely random, identifying persistent patterns or recurring behaviors should be impossible. However, if distinct market states exist, it may be possible to characterize their behavior and study how they evolve over time.

Understanding this distinction is important because it affects how uncertainty, decision-making, and market behavior are interpreted.

---
## Research Question

The project seeks to answer the following questions:

- Can financial markets be segmented into distinct regimes?
- Do these regimes exhibit different behavioral characteristics?
- Are some regimes more persistent than others?
- How likely is the market to transition from one regime to another?
- Can transition dynamics provide useful information beyond regime identification itself?

---

## Dataset

The analysis is based on historical XAUUSD (Gold Spot) market data.
The dataset includes OHLCV information and derived market features used to characterize market behavior across multiple time horizons.

---

## Methodology

Market Data
      ↓
Feature Engineering
      ↓
Clustering
      ↓
Regime Characterization
      ↓
Target Analysis
      ↓
Markov Transition Modeling
      ↓
Transition-Based Target Analysis
      ↓
Validation & Out-of-Sample Evaluation

---
## Main Contributions

This project contributes by:

- Identifying market regimes using unsupervised learning.
- Characterizing each regime through volatility, efficiency, persistence, and order-flow features.
- Modeling regime evolution using Markov chains.
- Evaluating transition stability through persistence, duration, and entropy.
- Demonstrating that regime transitions contain more predictive information than isolated regimes.
- Validating transition behavior across validation and out-of-sample datasets.

---
## Results
### Regime Identification: One of the central questions of this project was whether financial markets behave as completely random systems or whether recurring structures can be identified through data.

The results suggest that market behavior is not entirely random. Distinct regimes emerged consistently across the analysis, exhibiting different characteristics in terms of efficiency, volatility, persistence, compression, and market activity.

These findings indicate that market dynamics may be organized into observable states rather than representing a purely chaotic process.

The identification of such regimes provides a structured framework for studying market behavior and evaluating how uncertainty evolves through time.

 "/content/drive/MyDrive/market_regime_project/results/figures/4H_regime_profiles.png"
### Cluster Characterization: While the clustering process successfully identified distinct market states, understanding what differentiates those states is essential for interpretation.

Once the regimes were identified, each cluster was analyzed using its average feature profile. The results showed that every regime exhibits a unique behavioral signature, characterized by different levels of efficiency, persistence, volatility, compression, market activity, and order-flow imbalance.

This step transforms clustering from a purely statistical exercise into an interpretable framework for describing market conditions.
"/content/drive/MyDrive/market_regime_project/results/figures/4H_regime_bars.png"

### Target Differentiation Across Regimes

To determine whether the identified regimes contain predictive information, several forward-looking targets were evaluated:

- Future Return
- Breakout Up
- Breakout Down
- Sharpe-like Ratio

Future return was considered the primary target; however, the results showed limited differentiation across clusters. In contrast, breakout-related targets displayed clearer differences, suggesting that the clustering process captures variations in directional pressure and market structure rather than direct return predictability.

/content/drive/MyDrive/market_regime_project/results/figures/4H/cluster_target_profiles.png"
### Regimen stability 
Since future returns alone did not strongly distinguish the regimes, the analysis shifted toward studying their temporal behavior.

For each regime, persistence, expected duration, and transition entropy were estimated. The results revealed substantial differences in stability, with some regimes remaining active for extended periods while others transitioned more frequently.

This finding suggests that the value of clustering lies not only in identifying market states but also in understanding how long those states tend to persist.

"/content/drive/MyDrive/market_regime_project/results/figures/4H/regime_stability.png"

### Markov Transition Modeling

A Markov framework was then used to model regime evolution through time.

Transition matrices were estimated to quantify:

Regime persistence
Expected duration
Transition probabilities
Transition uncertainty (entropy)

The analysis revealed dominant transition pathways and identified stable regimes that act as recurring states within the market structure.
/content/drive/MyDrive/market_regime_project/results/figures/4H/transition_network.png"

### Transition-Based Target Analysis

After evaluating the target behavior within each cluster, it was observed that future returns alone did not provide a strong separation between market regimes. While some differences existed, the clustering process was not able to identify regimes with consistently distinct return profiles.

To further investigate the information contained in the market states, the analysis was extended from individual clusters to regime transitions. Using the Markov framework, each observation was classified according to the transition between consecutive states (e.g., 0→3, 1→0, 2→3).

The resulting heatmap summarizes the average target behavior associated with each transition. Three target variables were analyzed:

* **Future Return:** average forward return after the transition.
* **Breakout Up:** probability of an upward breakout.
* **Breakout Down:** probability of a downward breakout.
/content/drive/MyDrive/market_regime_project/results/figures/4H/transition_target_heatmap.png"

### Research implications
The findings suggest that market behavior is better explained by regime evolution than by static regime identification alone.

While clustering provides a useful representation of market states, the transition dynamics between those states contain additional information regarding future market behavior. Consequently, the final stage of the research focuses on combining regime transitions with order-flow and market microstructure analysis to better understand the mechanisms driving directional market movements.

---
## Key findings

- Market regimes can be identified consistently across multiple timeframes.
- Regimes exhibit distinct structural characteristics.
- Future returns show limited separation at the cluster level.
- Regime stability differs substantially across states.
- Markov transitions reveal dominant market pathways.
- Transition dynamics contain more predictive information than isolated regimes.
- Several transition patterns remain robust out-of-sample.
---
## Validation vs Out-of-Sample Transition Analysis

To evaluate the robustness of the transition-based framework, the average future returns associated with the most relevant regime transitions were compared between the validation and out-of-sample datasets.

The results show that several transitions maintain positive returns across both samples, suggesting that part of the information extracted from the regime transition process generalizes beyond the calibration period.

Among the strongest transitions, **3→2** stands out as the most consistent pattern, exhibiting the highest average future return in both validation and out-of-sample data. Similarly, transitions **3→0**, **1→1**, and **0→1** maintain positive returns across both datasets, indicating a degree of stability in their directional behavior.

Interestingly, some transitions that exhibited weak or even negative returns during validation, such as **2→3** and **2→2**, showed substantially improved performance out-of-sample. This suggests that the predictive information contained within regime evolution may vary across market environments and reinforces the importance of evaluating transition dynamics under different market conditions.

A key observation is that transitions involving Clusters **2** and **3** repeatedly appear among the strongest performers in the out-of-sample dataset. This finding is consistent with the previous transition heatmap analysis, where these states exhibited distinctive breakout characteristics and directional behavior.

Overall, the results indicate that the predictive value is not concentrated in a single cluster but rather emerges from the interaction between regimes and their transition dynamics. Consequently, the analysis supports the use of a Markov-based framework to model market evolution and motivates the next stage of the research, where transition probabilities, persistence, and order flow characteristics will be combined to better understand the mechanisms driving future market movements.

/content/drive/MyDrive/market_regime_project/results/figures/4H/transition_validation_oos.png"
---

## Future Work

Future developments of the framework include:

- Regime-based risk characterization
- Multi-timeframe regime integration
- Market microstructure analysis using footprint data
- Decision tree models for regime classification
- Probabilistic forecasting and decision support systems
---
## Why This Project Matters

The objective of this project is not to predict prices directly.

Instead, it aims to develop a reproducible analytical framework for understanding complex dynamic systems through state identification, regime characterization, and transition analysis.

Although financial markets serve as the initial case study, the methodology can be extended to other domains where uncertainty, variability, and state transitions play a critical role in decision-making.

---
## Conclusion

The results suggest that financial markets cannot be fully described by static market states alone.

While clustering provides a useful representation of market structure, the most informative signals emerge from the transitions between regimes. Modeling these dynamics through Markov chains reveals persistence patterns, dominant transition pathways, and transition-specific behaviors that are not visible at the cluster level.

These findings support the idea that regime evolution may provide a more informative framework for understanding future market behavior than regime identification alone.

