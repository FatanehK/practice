'''Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''



def binary_search(array,target):
    low =0
    hi = len(array)-1

    while low <= hi:
        mid = low +(hi-low)//2
        if array[mid] == target:
            return mid
        elif array[mid]< target:
            low = mid+1
        else:
            hi = mid-1
    return -1
print(binary_search([-1, 0, 3, 5, 9, 12], 2))
