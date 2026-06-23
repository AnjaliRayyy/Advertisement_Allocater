# algorithms/priority_queue.py


import heapq


def priority_allocate(ads, slot_capacity):

    allocations = {}

    total_revenue = 0

    total_used_time = 0


    for slot_name, capacity in slot_capacity.items():

        heap = []


        for ad in ads:

            if ad["slot"] == slot_name:

                heapq.heappush(
                    heap,

                    (
                        -ad["priority"],

                        -ad["budget"],

                        ad
                    )
                )


        selected = []

        remaining = capacity

        revenue = 0


        while heap and remaining > 0:

            _, _, ad = heapq.heappop(heap)


            if ad["duration"] <= remaining:

                selected.append(ad)

                remaining -= ad["duration"]

                revenue += ad["budget"]


        allocations[slot_name] = {

            "ads": selected,

            "used_time":
            capacity - remaining,

            "remaining_time":
            remaining,

            "revenue":
            revenue
        }

        total_revenue += revenue

        total_used_time += (
            capacity - remaining
        )


    return {

        "algorithm":
        "Priority Queue",

        "allocations":
        allocations,

        "total_revenue":
        total_revenue,

        "total_used_time":
        total_used_time
    }