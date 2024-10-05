"""Given a binary array nums, return the maximum length of a contiguous subarray with an 
equal number of 0 and 1.
Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1."""


def contigous_array(nums):
    mx_length = 0
    cumulative_sum = 0
    sum_map = {0: -1}
    for i in range(len(nums)):
        if nums[i] == 1:
            cumulative_sum += 1
        else:
            cumulative_sum -= 1

        if cumulative_sum in sum_map:
            subarr_len = i - sum_map[cumulative_sum]
            mx_length = max(subarr_len, mx_length)
        else:
            sum_map[cumulative_sum] = i
    return mx_length


print(contigous_array([0, 1, 0, 0, 1, 1, 1]))
