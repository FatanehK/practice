"""Search in Rotated Array: Given a sorted array of n integers that has been 
rotated an unknown number of times, write code to find an element in the array. 
You may assume that the array was originally sorted in increasing order

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

"""


def search_rotated_sorted_arry(arry, target):
    left = 0
    right = len(arry) - 1
    while left <= right:
        mid = (right + left) // 2
        if arry[mid] == target:
            return mid
        # left sorted portion
        if arry[left] <= arry[mid]:
            if arry[left] <= target < arry[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # right sorted portion
            if arry[mid] < target <= arry[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(search_rotated_sorted_arry([3, 1], 1))
