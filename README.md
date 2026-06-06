## Overview

Financial markets are among the most widely used investment environments today, attracting participants with diverse backgrounds, objectives, and analytical approaches.

Despite the vast amount of available information and analytical tools, a common belief persists: financial markets are inherently chaotic and unpredictable due to the interaction of economic, political, social, and behavioral factors.

As a result, investors often rely on different perspectives to navigate uncertainty, including fundamental analysis, technical analysis, quantitative methods, and algorithmic strategies. However, many of these approaches focus on specific aspects of market behavior and may not fully explain how market conditions evolve through time.

This project was developed to investigate whether market behavior is truly random or whether identifiable structures emerge over time that can be studied systematically.

---

## Business Problem

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

The analytical framework follows the steps below:

1. Exploratory Data Analysis (EDA)

Market behavior was examined through descriptive statistics and distributional analysis to identify variability, volatility patterns, and structural characteristics.

2. Feature Engineering

Relevant variables were created to represent market dynamics and provide a foundation for regime identification.

3. Regime Detection

Clustering techniques were applied to identify groups of observations sharing similar characteristics.

Different timeframes were evaluated to assess the stability and reproducibility of the resulting regimes.

4. Regime Characterization

Each identified regime was analyzed in terms of return behavior, volatility profiles, persistence, and market conditions.

5. Transition Analysis

Markov chains were used to model regime transitions and evaluate how market states evolve through time.

---
## Results
### Regime Identification: One of the central questions of this project was whether financial markets behave as completely random systems or whether recurring structures can be identified through data.

The results suggest that market behavior is not entirely random. Distinct regimes emerged consistently across the analysis, exhibiting different characteristics in terms of efficiency, volatility, persistence, compression, and market activity.

These findings indicate that market dynamics may be organized into observable states rather than representing a purely chaotic process.

The identification of such regimes provides a structured framework for studying market behavior and evaluating how uncertainty evolves through time.

 "/content/drive/MyDrive/market_regime_project/results/figures/4H_regime_profiles.png"
### Cluster Characterization: While the clustering process successfully identified distinct market states, understanding what differentiates those states is essential for interpretation.

To address this, the average feature profile of each cluster was analyzed across key variables, including efficiency, persistence, compression, volatility, market activity, and order-flow imbalance.

The results suggest that each cluster exhibits a unique behavioral signature rather than representing arbitrary statistical groupings.

For example:
Cluster 2 exhibits the highest levels of efficiency and persistence, suggesting a more structured and stable market environment.
Cluster 3 is characterized by elevated compression and volatility, indicating a potentially transitional market state where accumulated pressure may lead to significant changes in market behavior.

Although these labels should be considered interpretative rather than definitive, they provide a useful framework for understanding how market conditions differ across regimes.

"/content/drive/MyDrive/market_regime_project/results/figures/4H_regime_bars.png"

The ability to characterize regimes based on observable market features transforms clustering from a purely mathematical exercise into a practical framework for studying market behavior. Rather than viewing the market as a homogeneous process, each regime can be analyzed as a distinct state with its own structural properties and transition dynamics.

### Target Differentiation Across Regimes

After identifying and characterizing the market regimes, the next objective was to evaluate whether these clusters were associated with different future outcomes. The purpose of this analysis was to determine whether regime identification could provide a measurable advantage for anticipating future market behavior.

Several target variables were selected for this evaluation:

* **Future Return:** to assess whether specific regimes were associated with superior future performance.
* **Breakout Up:** to measure the probability of an upward directional expansion.
* **Breakout Down:** to measure the probability of a downward directional expansion.
* **Sharpe-like Ratio:** to evaluate risk-adjusted performance across regimes.

Future return was considered the primary target because the ultimate objective of many market participants is to identify conditions associated with superior returns. However, the results suggest that the identified clusters do not exhibit substantial differences in future returns. Although some variation exists, the separation is not sufficiently strong to conclude that regime identification alone provides a reliable predictive advantage for price forecasting.

More noticeable differences emerge in breakout behavior. Certain clusters display a higher tendency toward upward expansions, while others exhibit a greater probability of downward breakouts. These findings suggest that the clustering process may be capturing meaningful differences in market structure and directional pressure, even if those differences are not yet reflected in future return distributions. This observation opens the possibility of further investigation using order flow and microstructural analysis to better understand the mechanisms driving these directional tendencies.

An equally important conclusion is that the absence of strong return differentiation does not invalidate the clustering process. Instead, it suggests that the primary value of regime identification may lie elsewhere. Rather than focusing exclusively on future returns, it becomes relevant to study how regimes behave through time, how stable they are, and how likely they are to transition into different states.

For this reason, the next stage of the analysis focuses on regime persistence, expected duration, and transition probabilities. By modeling the evolution of market states through Markov chains, it becomes possible to study not only the characteristics of each regime but also the dynamics governing how the market moves between them. This transition-based perspective may provide a more informative framework for anticipating future market conditions than return analysis alone.

/content/drive/MyDrive/market_regime_project/results/figures/4H/cluster_target_profiles.png"

---
### Regimen stability 
After evaluating several target variables, future returns showed limited differentiation across clusters. However, significant differences emerged when analyzing regime persistence and expected duration.

The results indicate that market states exhibit distinct temporal behaviors. Some regimes tend to remain active for prolonged periods, while others transition more frequently.

In the 4H timeframe, Cluster 3 displayed the highest persistence (85%) and the longest expected duration (6.81 periods), suggesting a particularly stable market state. Conversely, Cluster 1 exhibited the lowest stability, remaining active for shorter periods before transitioning.

These findings suggest that the primary value of clustering may not lie in predicting returns directly, but rather in identifying market states with different stability characteristics. This naturally motivates the use of Markov chains to study transition probabilities and the evolution of market regimes over time

"/content/drive/MyDrive/market_regime_project/results/figures/4H/regime_stability.png"
---
### Regime Transition Analysis

After identifying the market regimes through clustering, the next step was to study how the market moves from one regime to another over time.

Rather than treating clusters as isolated states, a Markov framework was used to model the transition dynamics between regimes. This allows us to estimate the probability of remaining in a given state, the expected duration of each regime, and the most likely paths followed by the market.

The network representation below summarizes the most relevant regime transitions for the 4H timeframe.

Interpretation of the Network
Node size represents the expected duration of a regime.
Node color represents transition entropy, where greener nodes indicate more predictable behavior and redder nodes indicate greater uncertainty.
Edge thickness represents the probability of transitioning from one regime to another.

The results reveal that Cluster 3 is the most stable regime, exhibiting the longest expected duration and the lowest entropy. This suggests that once the market enters this state, its future behavior becomes more predictable compared to the other regimes.

Cluster 0 appears as a central transition hub, receiving the majority of transitions originating from other regimes. Both Cluster 1 and Cluster 2 exhibit strong tendencies to transition toward Cluster 0, indicating that this state may represent a common intermediate market condition.

The strongest transition pathways observed are:

Cluster 1 → Cluster 0
Cluster 2 → Cluster 0
Cluster 3 → Cluster 0

These transitions form the dominant regime flow observed throughout the sample.
/content/drive/MyDrive/market_regime_project/results/figures/4H/transition_network.png"
---
##### Transition-Based Target Analysis

After evaluating the target behavior within each cluster, it was observed that future returns alone did not provide a strong separation between market regimes. While some differences existed, the clustering process was not able to identify regimes with consistently distinct return profiles.

To further investigate the information contained in the market states, the analysis was extended from individual clusters to regime transitions. Using the Markov framework, each observation was classified according to the transition between consecutive states (e.g., 0→3, 1→0, 2→3).

The resulting heatmap summarizes the average target behavior associated with each transition. Three target variables were analyzed:

* **Future Return:** average forward return after the transition.
* **Breakout Up:** probability of an upward breakout.
* **Breakout Down:** probability of a downward breakout.

### Key Findings

The analysis reveals that the transition itself contains more information than the isolated cluster.

The strongest positive future returns are concentrated in transitions such as:

* **0→3**
* **1→0**
* **0→2**
* **3→2**

These transitions also exhibit relatively high probabilities of upward breakouts, suggesting that changes in market state may contain predictive information regarding future directional movement.

Conversely, transitions such as:

* **1→3**
* **2→3**
* **3→1**
* **3→3**

show negative average future returns and significantly higher probabilities of downward breakouts. In particular, transitions ending in or remaining within Cluster 3 appear associated with increased downside risk.

### Interpretation

These results suggest that market structure is not fully captured by static regime identification. Instead, the evolution of the market from one regime to another provides additional information regarding future behavior.

This finding motivates the use of Markov transition dynamics as a complementary layer to clustering. Rather than asking:

> Which cluster produces the highest return?

the more relevant question becomes:

> What is the probability of moving to the next regime, and how does that transition affect future market behavior?

The transition framework therefore becomes the foundation for the next stage of the research, where order flow and market microstructure variables will be analyzed conditional on specific regime transitions in order to better understand the mechanisms driving directional market movements.
/content/drive/MyDrive/market_regime_project/results/figures/4H/transition_target_heatmap.png"
---
## Key Findings

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

