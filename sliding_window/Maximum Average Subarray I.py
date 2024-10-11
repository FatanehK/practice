"""You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000"""


def findMaxAverage(nums, k):
    l = 0
    curr_sum = 0
    max_average = float("-inf")
    for r in range(k):
        curr_sum += nums[r]
    max_average = curr_sum / k

    for r in range(k,len(nums)):
        curr_sum += nums[r]
        curr_sum -=nums[l]
        l+=1
        avg = curr_sum / k
        max_average = max(max_average, avg)
    return max_average


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
