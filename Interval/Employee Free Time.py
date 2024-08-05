"""Write a function to find the common free time for all employees from a 
list called schedule. Each employee's schedule is represented by a list of 
non-overlapping intervals sorted by start times. 
The function should return a list of finite, non-zero length intervals where all employees are free, also sorted in order.

EXAMPLES
Input:

schedule = [[[2,4],[7,10]],[[1,5]],[[6,9]]]
Output:

[(5,6)]
Explanation: The three employees collectively have only one common free time interval, which is from 5 to 6."""


def employee_free_time(schedule):
    output =[]
    flattend= [ i for employee in schedule for i in employee]
    print(flattend)
    intervals = sorted(flattend, key=lambda x: x[0])
    print(intervals)
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        start = intervals[i][0]
        if start < intervals[i - 1][1]:
            result[-1] = [
                min(start, intervals[i - 1][0]),
                max(intervals[i][1], intervals[i - 1][1]),
            ]
        else:
            result.append(intervals[i])
    if len(result)== 1:
        return output
    else: 
        for i in range(1,len(result)):
            start = result[i-1][1]
            end = result[i][0]
        output.append((start,end))

    return output
print(employee_free_time([[[2, 4], [7, 10]], [[1, 5]], [[6, 9]]]))
