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
    zero = 0
    one = 0
    map = {}  # count[1]-count[0]---> indx
    result = 0
    for i, num in enumerate(nums):
        if num == 0:
            zero += 1
        else:
            one += 1

        if one - zero not in map:
            map[one - zero] = i
        if one == zero:
            result = one + zero
        else:
            indx = map[one - zero]
            result = max(result, i - indx)
    return result


print(contigous_array([0, 1, 0, 0, 1, 1, 1]))
