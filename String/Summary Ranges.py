"""You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9" 
"""
def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    result = []
    start = nums[0]
    end =None
    for i in range(len(nums)):
        if nums[i]+1 in nums:
            continue
        else:
            end = nums[i]
            if end == start:
                result.append(str(start))
            else:
                result.append(str(start)+"->"+str(end))
            if i < len(nums)-1:
                start = nums[i+1]
                end =None
    return result
print(summaryRanges([0, 1, 2, 4, 5, 7]))
