# utils/metrics.py

import time
import pandas as pd


def benchmark_algorithm(
    algorithm_function,
    ads,
    slot_capacity
):
    """
    Measures execution time
    """

    start_time = time.perf_counter()

    result = algorithm_function(
        ads,
        slot_capacity
    )

    end_time = time.perf_counter()

    runtime = (
        end_time - start_time
    ) * 1000


    result["runtime_ms"] = round(
        runtime,
        4
    )

    return result


def calculate_utilization(
    total_used_time,
    slot_capacity
):
    """
    Calculates utilization %
    """

    total_capacity = sum(
        slot_capacity.values()
    )

    utilization = (

        total_used_time /

        total_capacity

    ) * 100


    return round(
        utilization,
        2
    )


def create_comparison_dataframe(
    results,
    slot_capacity
):
    """
    Creates comparison table
    """

    comparison_data = []


    for result in results:

        utilization = (
            calculate_utilization(
                result[
                    "total_used_time"
                ],
                slot_capacity
            )
        )


        comparison_data.append({

            "Algorithm":
            result["algorithm"],

            "Revenue":
            result["total_revenue"],

            "Runtime(ms)":
            result["runtime_ms"],

            "Utilization(%)":
            utilization
        })


    df = pd.DataFrame(
        comparison_data
    )

    return df


def export_allocation_csv(
    result,
    filename=
    "allocation_report.csv"
):
    """
    Export allocation results
    """

    rows = []


    for slot_name, data in (
        result[
            "allocations"
        ].items()
    ):

        for ad in data["ads"]:

            rows.append({

                "Algorithm":
                result["algorithm"],

                "Slot":
                slot_name,

                "Ad_ID":
                ad["id"],

                "Duration":
                ad["duration"],

                "Budget":
                ad["budget"],

                "Priority":
                ad["priority"]
            })


    df = pd.DataFrame(rows)

    df.to_csv(
        filename,
        index=False
    )

    return filename