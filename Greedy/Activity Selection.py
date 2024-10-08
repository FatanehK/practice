# You are given n activities with their start and finish times.
# Select the maximum number of activities that can be performed by a single person,
# assuming that a person can only work on a single activity at a time.

# start_times = [1, 3, 0, 5, 8, 5]


# # List of end times
# end_times = [2, 4, 6, 7, 9, 9]
def max_number_activity(start_times, end_times):
    mx_num_activity = 1
    activity = sorted(zip(start_times, end_times), key=lambda x: x[1])
    # (1,2),(3,4),(0,6),(5,7),(8,9),(5,9)
    end = activity[0][1]
    for i in range(1, len(activity)):
        start_time = activity[i][0]
        if start_time > end:
            mx_num_activity += 1
            end = activity[i][1]

    return mx_num_activity


print(max_number_activity([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
activities = [
    ("A1", 1, 2),
    ("A2", 3, 4),
    ("A3", 0, 6),
    ("A4", 5, 7),
    ("A5", 8, 9),
    ("A6", 5, 9),
]


def max_activity_func(activities):
    activities.sort(key=lambda x: x[2])
    max_acti = 1
    end = activities[0][2]
    for i in range(1, len(activities)):
        start = activities[i][1]
        if start > end:
            max_acti += 1
            end = activities[i][2]
    return max_acti


print(max_activity_func(activities))
