'''You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

'''
def maxium_sum(nums):
    max_arr = -1

    def transform(n):
        tem = n
        sum = 0
        while tem > 0:
            sum += tem % 10
            tem = tem//10
        return sum


    hash_map = {}
    for num in nums:
        digitsum = transform(num)
        if digitsum in hash_map:
            max_arr = max(max_arr, num+hash_map[digitsum])
        if digitsum not in hash_map:
            hash_map[digitsum] = num 

    return max_arr


print(maxium_sum([18,43,36,13,7]))