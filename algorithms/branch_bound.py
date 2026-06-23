# algorithms/branch_bound.py


class Node:

    def __init__(
        self,
        level,
        revenue,
        duration,
        selected
    ):

        self.level = level

        self.revenue = revenue

        self.duration = duration

        self.selected = selected

        self.bound = 0


def calculate_bound(
    node,
    ads,
    capacity
):

    if node.duration >= capacity:
        return 0

    bound = node.revenue

    total_duration = node.duration

    j = node.level + 1


    while (
        j < len(ads)
        and
        total_duration +
        ads[j]["duration"]
        <= capacity
    ):

        total_duration += ads[j]["duration"]

        bound += ads[j]["budget"]

        j += 1


    # fractional estimate
    if j < len(ads):

        remaining = (
            capacity - total_duration
        )

        bound += (

            remaining *

            ads[j]["budget"] /

            ads[j]["duration"]
        )

    return bound


def solve_branch_bound(
    ads,
    capacity
):

    ads.sort(

        key=lambda x:
        x["budget"] / x["duration"],

        reverse=True
    )


    queue = []

    root = Node(
        -1,
        0,
        0,
        []
    )

    root.bound = calculate_bound(
        root,
        ads,
        capacity
    )

    queue.append(root)

    max_revenue = 0

    best_ads = []


    while queue:

        node = queue.pop(0)


        if (
            node.level ==
            len(ads) - 1
        ):
            continue


        next_level = (
            node.level + 1
        )

        current_ad = ads[next_level]


        # Include ad
        include = Node(

            next_level,

            node.revenue +
            current_ad["budget"],

            node.duration +
            current_ad["duration"],

            node.selected +
            [current_ad]
        )


        if (

            include.duration <= capacity

            and

            include.revenue >
            max_revenue
        ):

            max_revenue = (
                include.revenue
            )

            best_ads = (
                include.selected
            )


        include.bound = (
            calculate_bound(
                include,
                ads,
                capacity
            )
        )


        if (
            include.bound >
            max_revenue
        ):

            queue.append(include)


        # Exclude ad
        exclude = Node(

            next_level,

            node.revenue,

            node.duration,

            node.selected
        )

        exclude.bound = (
            calculate_bound(
                exclude,
                ads,
                capacity
            )
        )


        if (
            exclude.bound >
            max_revenue
        ):

            queue.append(exclude)


    used_time = 0

    for ad in best_ads:
        used_time += ad["duration"]


    return {

        "ads": best_ads,

        "used_time": used_time,

        "remaining_time":
        capacity - used_time,

        "revenue":
        max_revenue
    }


def branch_bound_allocate(
    ads,
    slot_capacity
):

    allocations = {}

    total_revenue = 0

    total_used_time = 0


    for slot_name, capacity in slot_capacity.items():

        slot_ads = []

        for ad in ads:

            if ad["slot"] == slot_name:
                slot_ads.append(ad)


        result = solve_branch_bound(
            slot_ads,
            capacity
        )

        allocations[slot_name] = result

        total_revenue += result["revenue"]

        total_used_time += result["used_time"]


    return {

        "algorithm":
        "Branch and Bound",

        "allocations":
        allocations,

        "total_revenue":
        total_revenue,

        "total_used_time":
        total_used_time
    }