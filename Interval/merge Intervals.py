def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        prve_end = result[-1][1]
        prve_start = result[-1][0]
        if prve_end >= intervals[i][0]:
            result[-1] = [prve_start, max(prve_end, intervals[i][1])]
        else:
            result.append(intervals[i])
    return result


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
