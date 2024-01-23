'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
# Boyer-Moore Voting Algorithm
def majorityElement(nums):
    result =0
    count =0
    for n in nums:
        if count == 0:
            result = n
        if n == result:
            count+=1
        else:
            count-=1
    return result 

print(majorityElement([8,6,8,8,6]))