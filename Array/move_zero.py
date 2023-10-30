'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]'''

def move_zero(arr):
    j=0
    for r in range(len(arr)):
        if arr[r]:
            arr[r],arr[j]= arr[j],arr[r]
            j+=1
    return j

    # i=0 
    # j=0
    # while i < len(nums):
    #     if nums[i] != 0:
    #         nums[i],nums[j]= nums[j],nums[i]
    #         j+=1
    #     i+=1
    # return nums
        
        
print(move_zero([1,1,2,0,9,9]))
def remove_duplicate(nums):
    j=1
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums[j] = nums[i]
            j+=1
        i+=1
    return nums
print(remove_duplicate([0,1,1,2,9,9]))