import os

import numpy as np
import pandas as pd
import networkx as nx

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def plot_cluster_distribution(
    df,
    output_dir
):

    plt.figure(figsize=(8, 5))

    sns.countplot(
        x="cluster",
        data=df,
        order=sorted(df["cluster"].unique())
    )

    plt.title("Cluster Distribution")
    plt.xlabel("Cluster")
    plt.ylabel("Observations")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "cluster_distribution.png"
        )
    )

    plt.close()

def plot_cluster_returns(
    df,
    output_dir
):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="cluster",
        y="future_return"
    )

    plt.title("Future Return by Cluster")

    plt.xlabel("Cluster")
    plt.ylabel("Future Return")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "cluster_returns.png"
        )
    )

    plt.close()

def plot_transition_matrix(
    df,
    output_dir
):

    transition_matrix = pd.crosstab(
        df["cluster"],
        df["cluster"].shift(-1),
        normalize="index"
    )

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        transition_matrix,
        annot=True,
        fmt=".2f",
        cmap="Blues"
    )

    plt.title("Transition Matrix")

    plt.xlabel("Next Cluster")
    plt.ylabel("Current Cluster")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "transition_matrix.png"
        )
    )

    plt.close()

def plot_persistence_analysis(
    df,
    output_dir
):

    transition_matrix = pd.crosstab(
        df["cluster"],
        df["cluster"].shift(-1),
        normalize="index"
    )

    persistence = np.diag(
        transition_matrix.values
    )

    persistence_df = pd.DataFrame({

        "cluster": transition_matrix.index,

        "persistence": persistence

    })

    plt.figure(figsize=(8, 5))

    sns.barplot(
        data=persistence_df,
        x="cluster",
        y="persistence"
    )

    plt.title(
        "Cluster Persistence"
    )

    plt.xlabel(
        "Cluster"
    )

    plt.ylabel(
        "Persistence Probability"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "persistence_analysis.png"
        )
    )

    plt.close()

def plot_regime_timeline(
    df,
    output_dir
):

    print("ENTRANDO A plot_regime_timeline")
    print("Output:", output_dir)
    print("Shape:", df.shape)
    fig, ax = plt.subplots(
        figsize=(16, 6)
    )

    price_col = "[Close]"

    ax.plot(
        df.index,
        df[price_col],
        linewidth=1
    )

    scatter = ax.scatter(
        df.index,
        df[price_col],
        c=df["cluster"],
        cmap="tab10",
        s=8
    )

    plt.colorbar(
        scatter,
        label="Cluster"
    )

    save_path = os.path.join(
        output_dir,
        "regime_timeline.png"
    )

    print("Guardando en:", save_path)

    plt.savefig(save_path)

    plt.close()

    print("Timeline guardado")

from sklearn.preprocessing import MinMaxScaler

def plot_cluster_targets(
    stats,
    timeframe,
    output_dir
):

    target_df = pd.DataFrame({

        "Future Return":
            stats[("future_return","mean")],

        "Sharpe Like":
            stats[("future_return","sharpe_like")],

        "Breakout Up":
            stats[("breakout_up","mean")],

        "Breakout Down":
            stats[("breakout_down","mean")]

    })

    scaler = MinMaxScaler()

    target_scaled = pd.DataFrame(
        scaler.fit_transform(target_df),
        columns=target_df.columns,
        index=target_df.index
    )

    target_scaled.T.plot(
        kind="bar",
        figsize=(12,6)
    )

    plt.title(
        f"{timeframe} Cluster Target Profiles"
    )

    plt.xlabel("Target")
    plt.ylabel("Normalized Value")

    plt.legend(
        title="Cluster"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "cluster_target_profiles.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def plot_transition_statistics(
    stats,
    timeframe,
    output_dir
):

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(15,5)
    )

    sns.barplot(
        data=stats,
        x=stats.index,
        y="persistence",
        ax=axes[0]
    )

    axes[0].set_title(
        "Persistence"
    )

    sns.barplot(
        data=stats,
        x=stats.index,
        y="expected_duration",
        ax=axes[1]
    )

    axes[1].set_title(
        "Expected Duration"
    )

    sns.barplot(
        data=stats,
        x=stats.index,
        y="entropy",
        ax=axes[2]
    )

    axes[2].set_title(
        "Entropy"
    )

    plt.suptitle(
        f"{timeframe} Transition Statistics"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "transition_statistics.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
    
def plot_regime_stability(
    stats,
    timeframe,
    output_dir
):

    from sklearn.preprocessing import MinMaxScaler

    stability_df = stats[
        [
            "persistence",
            "expected_duration"
        ]
    ].copy()

    scaler = MinMaxScaler()

    stability_scaled = pd.DataFrame(
        scaler.fit_transform(stability_df),
        columns=stability_df.columns,
        index=stability_df.index
    )

    plt.figure(figsize=(8,5))

    sns.heatmap(
        stability_scaled,
        annot=stability_df.round(2),
        fmt="",
        cmap="RdYlBu_r",
        linewidths=0.5
    )

    plt.title(
        f"{timeframe} Regime Stability"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "regime_stability.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

print("ENTRANDO A plot_transition_network")

#grafo
def plot_transition_network(
    matrix,
    transition_stats,
    timeframe,
    output_dir
    
):
    matrix.columns = (
        matrix.columns.astype(int)
    )
    
    G = nx.DiGraph()

    # -----------------------
    # Nodos
    # -----------------------

    for cluster in matrix.index:

        G.add_node(
            cluster,
            duration=transition_stats.loc[
                cluster,
                "expected_duration"
            ],
            entropy=transition_stats.loc[
                cluster,
                "entropy"
            ]
        )

    # -----------------------
    # Flechas
    # -----------------------

    for source in matrix.index:

        for target in matrix.columns:

            prob = matrix.loc[source, (target)]

            if source == int(target):
                continue

            if prob < 0.05:
                continue

            G.add_edge(
                source,
                int(target),
                weight=prob
            )

    plt.figure(figsize=(10,8))

    pos = nx.spring_layout(
        G,
        seed=42
    )

    node_sizes = [

        G.nodes[n]["duration"] * 800

        for n in G.nodes()

    ]

    node_colors = [

        G.nodes[n]["entropy"]

        for n in G.nodes()

    ]

    edge_widths = [

        G[u][v]["weight"] * 20

        for u,v in G.edges()

    ]
    print("ENTRANDO A plot_transition_network")
    print("Nodos:", G.nodes())
    print("Edges:", G.edges())
    print("Output dir:")
    print(output_dir)
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_sizes,
        node_color=node_colors,
        cmap="RdYlGn_r"
    )

    nx.draw_networkx_labels(
        G,
        pos
    )

    nx.draw_networkx_edges(
        G,
        pos,
        width=edge_widths,
        arrows=True
    )

    plt.title(
        f"{timeframe} Regime Transition Network"
    )

    plt.axis("off")

    save_path = os.path.join(
    output_dir,
    "transition_network.png"
    )

    print("Guardando en:")
    print(save_path)

    plt.savefig(
    save_path,
    dpi=300,
    bbox_inches="tight"
    )

    print("Guardado correctamente")

    plt.close()
    
import networkx as nx
print("ENTRANDO A plot_transition_network")
def plot_transition_network(
    transition_matrix,
    transition_stats,
    timeframe,
    output_dir
):

    G = nx.DiGraph()

    # Nodos
    for cluster in transition_matrix.index:

        G.add_node(
            int(cluster),
            duration=transition_stats.loc[
                cluster,
                "expected_duration"
            ],
            entropy=transition_stats.loc[
                cluster,
                "entropy"
            ]
        )

    # Aristas
    for source in transition_matrix.index:

        for target in transition_matrix.columns:

            prob = transition_matrix.loc[
                source,
                target
            ]

            source_int = int(source)
            target_int = int(target)

            if source_int == target_int:
                continue

            if prob < 0.05:
                continue

            G.add_edge(
                source_int,
                target_int,
                weight=float(prob)
            )

    plt.figure(figsize=(10,8))

    pos = nx.spring_layout(
        G,
        seed=42,
        k=2
    )

    node_sizes = [
        G.nodes[n]["duration"] * 1200
        for n in G.nodes()
    ]

    node_colors = [
        G.nodes[n]["entropy"]
        for n in G.nodes()
    ]

    edge_widths = [
        G[u][v]["weight"] * 50
        for u,v in G.edges()
    ]

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_sizes,
        node_color=node_colors,
        cmap="RdYlGn_r"
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=12,
        font_weight="bold"
    )

    nx.draw_networkx_edges(
        G,
        pos,
        width=edge_widths,
        arrows=True,
        arrowsize=25
    )

    plt.title(
        f"{timeframe} Regime Transition Network"
    )

    plt.axis("off")

    plt.tight_layout()

    print(f"Guardando grafo {timeframe}")

    print(
        os.path.join(
        output_dir,
        "transition_network.png"
    )
)

    plt.savefig(
        os.path.join(
            output_dir,
            "transition_network.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )
    print("TRANSITION NETWORK GUARDADO")
    plt.close()
    
from sklearn.preprocessing import MinMaxScaler
def plot_transition_target_heatmap(
    transition_stats,
    timeframe,
    output_dir
):

    scaler = MinMaxScaler()

    scaled = pd.DataFrame(
        scaler.fit_transform(
            transition_stats
        ),
        columns=transition_stats.columns,
        index=transition_stats.index
    )

    plt.figure(
        figsize=(10,8)
    )

    sns.heatmap(
        scaled,
        annot=transition_stats.round(3),
        fmt="",
        cmap="RdYlGn",
        linewidths=0.5
    )

    plt.title(
        f"{timeframe} Transition Target Heatmap"
    )

    plt.ylabel(
        "Transition"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "transition_target_heatmap.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
def plot_transition_validation_oos(
    comparison_df,
    timeframe,
    output_dir
):

    plt.figure(figsize=(12,6))

    comparison_df.plot(
        kind="bar",
        ax=plt.gca()
    )

    plt.title(
        f"{timeframe} Validation vs OOS Returns"
    )

    plt.ylabel(
        "Mean Future Return"
    )

    plt.xlabel(
        "Transition"
    )

    plt.grid(
        axis="y",
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "transition_validation_oos.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
