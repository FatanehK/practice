"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104"""


def Merge_Intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(len(intervals)):
        curr_start, curr_end = intervals[i][0], intervals[i][1]
        prev_start, prev_end = result[-1][0],result[-1][1]

        if curr_start <= prev_end:
            result[-1] = [prev_start, max(curr_end, prev_end)]
        else:
            result.append([curr_start, curr_end])
    return result
    


print(Merge_Intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
