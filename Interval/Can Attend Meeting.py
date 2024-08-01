"""Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1, determine if there are any overlapping meetings. If there is no overlap between any meetings, return true; otherwise, return false.

Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.

EXAMPLES
Input:

intervals = [(1,5),(3,9),(6,8)]
Output:

false"""
def can_attend_meeting(intervals):
    intervals.sort(key = lambda x:x[0])
    for i in range(1,len(intervals)):
        start = intervals[i][0]
        prev_end = intervals[i-1][1]
        if start < prev_end:
            return False
    return True

print(can_attend_meeting([(1, 5), (3, 9), (6, 8)]))
