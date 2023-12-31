'''Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.

A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

Example 1:

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
Example 2:

Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.
 '''


def isMajorityElement(nums, target):
    left= getleftmostindex(nums, target)
    right = getrightmostindex(nums,target)
    if right - left + 1 > len(nums)/2:
        return True
    return False


def getleftmostindex(nums, target):
    high= len(nums)-1
    low =0
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] >= target:

            high = mid-1
        else:
            low = mid+1
    return low

def getrightmostindex(nums,target):

    high = len(nums)-1
    low = 0
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] <= target:

            low = mid+1
        else:
            high = mid -1

    return low-1
print(isMajorityElement([2,4,5,5,5,5,5,6,6],5))