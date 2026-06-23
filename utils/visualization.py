# utils/visualization.py

import matplotlib.pyplot as plt


def plot_revenue_chart(
    comparison_df
):
    """
    Revenue bar chart
    """

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.bar(

        comparison_df[
            "Algorithm"
        ],

        comparison_df[
            "Revenue"
        ]
    )

    ax.set_title(
        "Revenue Comparison"
    )

    ax.set_ylabel(
        "Revenue"
    )

    ax.set_xlabel(
        "Algorithms"
    )

    plt.xticks(
        rotation=20
    )

    return fig


def plot_runtime_chart(
    comparison_df
):
    """
    Runtime comparison
    """

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.bar(

        comparison_df[
            "Algorithm"
        ],

        comparison_df[
            "Runtime(ms)"
        ]
    )

    ax.set_title(
        "Runtime Comparison"
    )

    ax.set_ylabel(
        "Milliseconds"
    )

    ax.set_xlabel(
        "Algorithms"
    )

    plt.xticks(
        rotation=20
    )

    return fig


def plot_utilization_chart(
    comparison_df
):
    """
    Slot utilization chart
    """

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.bar(

        comparison_df[
            "Algorithm"
        ],

        comparison_df[
            "Utilization(%)"
        ]
    )

    ax.set_title(
        "Slot Utilization"
    )

    ax.set_ylabel(
        "Utilization %"
    )

    ax.set_xlabel(
        "Algorithms"
    )

    plt.xticks(
        rotation=20
    )

    return fig