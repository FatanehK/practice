"""Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""


def max_product(nums):

    min_prod = nums[0]
    mx_prod = nums[0]
    result = nums[0]
    for num in nums[1:]:
        if num < 0:
            min_prod, mx_prod = mx_prod, min_prod
        min_prod = min(min_prod * num, num)
        mx_prod = max(num * mx_prod, num)
        result = max(mx_prod, result)
    return result 


print(max_product([-2, 0, -1]))
