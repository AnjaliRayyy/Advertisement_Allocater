# algorithms/greedy.py


def greedy_allocate(ads, slot_capacity):

    allocations = {}

    total_revenue = 0

    total_used_time = 0


    for slot_name, capacity in slot_capacity.items():

        slot_ads = []

        for ad in ads:
            if ad["slot"] == slot_name:
                slot_ads.append(ad)


        slot_ads.sort(
            key=lambda x:
            x["budget"] / x["duration"],
            reverse=True
        )


        selected = []

        remaining = capacity

        revenue = 0


        for ad in slot_ads:

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
        "Greedy",

        "allocations":
        allocations,

        "total_revenue":
        total_revenue,

        "total_used_time":
        total_used_time
    }