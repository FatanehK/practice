"""Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)



(0,8),(8,10) is not conflict at 8

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        print(start)
        print(end)

        s = 0
        e = 0
        count = 0
        result = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1

            else:
                # if end and start the same increae e pointer
                e += 1
                count -= 1
            result = max(result, count)
        return result


sol = Solution()
print(sol.min_meeting_rooms([Interval(0, 30), Interval(7, 10), Interval(1, 20)]))
