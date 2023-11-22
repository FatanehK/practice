"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.



Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
"""


class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
            prev_e = intervals[i - 1]
            new_start = intervals[i]
            if new_start.start < prev_e.end:
                return False
        return True


sol = Solution()
print(sol.can_attend_meetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
