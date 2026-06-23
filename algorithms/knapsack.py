# algorithms/knapsack.py


def solve_knapsack(slot_ads, capacity):

    n = len(slot_ads)

    # DP table
    dp = [
        [0 for _ in range(capacity + 1)]
        for _ in range(n + 1)
    ]


    # Build DP table
    for i in range(1, n + 1):

        duration = slot_ads[i - 1]["duration"]

        budget = slot_ads[i - 1]["budget"]

        for w in range(capacity + 1):

            if duration <= w:

                dp[i][w] = max(
                    budget +
                    dp[i - 1][w - duration],

                    dp[i - 1][w]
                )

            else:

                dp[i][w] = dp[i - 1][w]


    # Backtracking selected ads
    selected = []

    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            ad = slot_ads[i - 1]

            selected.append(ad)

            w -= ad["duration"]


    total_revenue = dp[n][capacity]

    used_time = capacity - w


    return {

        "ads": selected,

        "used_time": used_time,

        "remaining_time": w,

        "revenue": total_revenue
    }


def knapsack_allocate(ads, slot_capacity):

    allocations = {}

    total_revenue = 0

    total_used_time = 0


    for slot_name, capacity in slot_capacity.items():

        slot_ads = []

        for ad in ads:

            if ad["slot"] == slot_name:
                slot_ads.append(ad)


        result = solve_knapsack(
            slot_ads,
            capacity
        )

        allocations[slot_name] = result

        total_revenue += result["revenue"]

        total_used_time += result["used_time"]


    return {

        "algorithm":
        "Dynamic Programming",

        "allocations":
        allocations,

        "total_revenue":
        total_revenue,

        "total_used_time":
        total_used_time
    }