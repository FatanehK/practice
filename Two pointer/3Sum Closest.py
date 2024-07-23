"""Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""


class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        closest_sum = float("inf")

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum_num = n + nums[l] + nums[r]
                if abs(sum_num - target) < abs(closest_sum - target):
                    closest_sum = sum_num

                if sum_num < target:
                    l += 1
                elif sum_num > target:
                    r -= 1
                else:
                    return sum_num

        return closest_sum


sol = Solution()
sol.threeSumClosest([-1, 2, 1, -4], 1)
