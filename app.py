# app.py

import streamlit as st
import pandas as pd

# utilities
from utils.parser import (
    parse_uploaded_file,
    dataframe_to_ads
)

from utils.metrics import (
    benchmark_algorithm,
    create_comparison_dataframe,
    export_allocation_csv,
    calculate_utilization
)

from utils.visualization import (
    plot_revenue_chart,
    plot_runtime_chart,
    plot_utilization_chart
)

# algorithms
from algorithms.greedy import greedy_allocate
from algorithms.priority_queue import priority_allocate
from algorithms.knapsack import knapsack_allocate
from algorithms.branch_bound import branch_bound_allocate


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Ad Slot Allocation System",
    layout="wide"
)

st.title("📺 Advertisement Slot Allocation System")
st.subheader(
    "Comparative Analysis of DSA Algorithms for Revenue Maximization"
)

st.markdown("---")


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Configuration")

algorithm_choice = st.sidebar.selectbox(
    "Select Algorithm",
    [
        "Greedy",
        "Priority Queue",
        "Dynamic Programming",
        "Branch and Bound",
        "Run All"
    ]
)

st.sidebar.markdown("### Slot Capacities (seconds)")

morning_slot = st.sidebar.number_input(
    "Morning Slot",
    min_value=10,
    value=120
)

prime_slot = st.sidebar.number_input(
    "PrimeTime Slot",
    min_value=10,
    value=150
)

evening_slot = st.sidebar.number_input(
    "Evening Slot",
    min_value=10,
    value=180
)

slot_capacity = {
    "Morning": morning_slot,
    "PrimeTime": prime_slot,
    "Evening": evening_slot
}


# -----------------------------
# File Upload
# -----------------------------
st.header("1. Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload .txt dataset",
    type=["txt", "csv"]
)

if uploaded_file is None:
    st.info("Upload dataset to begin.")
    st.stop()


# -----------------------------
# Parse File
# -----------------------------
try:
    df = parse_uploaded_file(
        uploaded_file
    )

    ads = dataframe_to_ads(df)

    st.success(
        "Dataset uploaded successfully"
    )

except Exception as e:

    st.error(
        f"Dataset Error: {e}"
    )

    st.stop()


# -----------------------------
# Dataset Preview
# -----------------------------
st.header("2. Dataset Preview")

st.dataframe(df)

st.markdown("---")


# -----------------------------
# Run Algorithms
# -----------------------------
st.header("3. Generate Allocation Plan")


def run_selected_algorithm():

    if algorithm_choice == "Greedy":

        return [

            benchmark_algorithm(
                greedy_allocate,
                ads,
                slot_capacity
            )
        ]

    elif algorithm_choice == "Priority Queue":

        return [

            benchmark_algorithm(
                priority_allocate,
                ads,
                slot_capacity
            )
        ]

    elif algorithm_choice == "Dynamic Programming":

        return [

            benchmark_algorithm(
                knapsack_allocate,
                ads,
                slot_capacity
            )
        ]

    elif algorithm_choice == "Branch and Bound":

        return [

            benchmark_algorithm(
                branch_bound_allocate,
                ads,
                slot_capacity
            )
        ]

    else:

        return [

            benchmark_algorithm(
                greedy_allocate,
                ads,
                slot_capacity
            ),

            benchmark_algorithm(
                priority_allocate,
                ads,
                slot_capacity
            ),

            benchmark_algorithm(
                knapsack_allocate,
                ads,
                slot_capacity
            ),

            benchmark_algorithm(
                branch_bound_allocate,
                ads,
                slot_capacity
            )
        ]


# -----------------------------
# Button
# -----------------------------
if st.button("Run Allocation"):

    results = run_selected_algorithm()

    st.success(
        "Allocation completed"
    )

    st.markdown("---")


    # =====================================
    # SINGLE ALGORITHM MODE
    # =====================================
    if len(results) == 1:

        result = results[0]

        st.header("Allocation Result")

        utilization = calculate_utilization(
            result["total_used_time"],
            slot_capacity
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Revenue",
            f"₹{result['total_revenue']}"
        )

        col2.metric(
            "Runtime",
            f"{result['runtime_ms']} ms"
        )

        col3.metric(
            "Utilization",
            f"{utilization}%"
        )


        # Allocation by slot
        for slot, data in result[
            "allocations"
        ].items():

            st.subheader(
                f"{slot} Slot"
            )

            if len(data["ads"]) == 0:

                st.warning(
                    "No ads allocated"
                )

                continue


            rows = []

            for ad in data["ads"]:

                rows.append({

                    "Ad ID":
                    ad["id"],

                    "Duration":
                    ad["duration"],

                    "Budget":
                    ad["budget"],

                    "Priority":
                    ad["priority"]
                })

            st.dataframe(
                pd.DataFrame(rows)
            )

            st.write(
                f"Revenue: ₹{data['revenue']}"
            )

            st.write(
                f"Used Time: {data['used_time']} sec"
            )

            st.write(
                f"Remaining Time: {data['remaining_time']} sec"
            )


        # Export
        csv_file = export_allocation_csv(
            result
        )

        with open(csv_file, "rb") as f:

            st.download_button(

                label="Download Allocation Report",

                data=f,

                file_name=
                "allocation_report.csv",

                mime="text/csv"
            )


    # =====================================
    # RUN ALL MODE
    # =====================================
    else:

        st.header(
            "Algorithm Comparison"
        )

        comparison_df = (
            create_comparison_dataframe(
                results,
                slot_capacity
            )
        )

        st.dataframe(
            comparison_df
        )


        # Charts
        st.subheader(
            "Revenue Comparison"
        )

        revenue_fig = (
            plot_revenue_chart(
                comparison_df
            )
        )

        st.pyplot(
            revenue_fig
        )


        st.subheader(
            "Runtime Comparison"
        )

        runtime_fig = (
            plot_runtime_chart(
                comparison_df
            )
        )

        st.pyplot(
            runtime_fig
        )


        st.subheader(
            "Slot Utilization Comparison"
        )

        utilization_fig = (
            plot_utilization_chart(
                comparison_df
            )
        )

        st.pyplot(
            utilization_fig
        )


        # Best algorithm
        best = comparison_df.loc[
            comparison_df[
                "Revenue"
            ].idxmax()
        ]

        st.success(

            f"Best Revenue Algorithm: "
            f"{best['Algorithm']} "
            f"(₹{best['Revenue']})"
        )