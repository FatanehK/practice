"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3"""

def remove_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    # find the intersection
    while True:
        slow= nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break
    # find duplicate
    slow = nums[0]
    while fast != slow :
        slow = nums[slow]
        fast = nums[fast]
    return slow
print(remove_duplicate([3, 1, 3, 4, 2]))
