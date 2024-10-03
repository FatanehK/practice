"""The objective of the “Meeting Rooms II” coding question is to determine the minimum number of 
conference rooms required to accommodate a set of meeting time intervals.
Given an array of intervals, where each interval represents 
a meeting with a start time and an exclusive end time, 
the task is to find the smallest number of rooms needed to hold all the meetings without any overlap."""
def min_number_of_meeting_room(intervals):
    start = sorted (i[0]for i in intervals)
    end = sorted(i[1] for i in intervals)
    used_room =0
    max_room = 0
    s_ptr=0
    e_ptr=0
    while s_ptr < len(intervals):
        if start[s_ptr] >= end[e_ptr]:
            used_room-=1
            e_ptr+=1
        else:
            s_ptr+=1
            used_room +=1 
        max_room = max(max_room, used_room)
    return max_room
print(min_number_of_meeting_room([[1, 5], [2, 6], [3, 8], [7, 10]]))
