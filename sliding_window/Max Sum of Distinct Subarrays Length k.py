"""Given an integer array nums and an integer k, write a function to identify the highest possible sum of a subarray within nums, where the subarray meets the following criteria: its length is k, and all of its elements are unique.

EXAMPLES
Example 1: Input:

nums = [3, 2, 2, 3, 4, 6, 7, 7, -1]
k = 4
output =20
Explanation: The subarrays of nums with length 4 are:

[3, 2, 2, 3] # elements 3 and 2 are repeated.
[2, 2, 3, 4] # element 2 is repeated.
[2, 3, 4, 6] # meets the requirements and has a sum of 15.
[3, 4, 6, 7] # meets the requirements and has a sum of 20.
[4, 6, 7, 7] # element 7 is repeated.
[6, 7, 7, -1] # element 7 is repeated.
We return 20 because it is the maximum subarray sum of all the subarrays that meet the conditions.
"""
def maxSum(nums,k):
    curr_sum =0 
    l =0
    max_sum =0
    state ={}

    for r in range(len(nums)):
        curr_sum += nums[r]
        state[nums[r]] = state.get(nums[r],0)+1

        if r-l+1 == k:
            if len(state)== k:
                max_sum = max(max_sum,curr_sum)
            curr_sum -= nums[l]
            state[nums[l]]-= 1
            if state[nums[l]]== 0:
                del state[nums[l]]
            l+=1
    return max_sum
print(maxSum([3, 2, 2, 3, 4, 6, 7, 7, -1],4))