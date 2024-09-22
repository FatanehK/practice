"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107"""


def subarray_sum(nums, k):
    prefix_sum = {0: 1}#----> diff if zero
    curr_sum = 0
    result = 0
    for num in nums:
        curr_sum += num

        diff = curr_sum - k
        result += prefix_sum.get(diff, 0)
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
    return result


print(subarray_sum([1, 2, 3], 3))
