"""You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100"""


def targetIndices(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def first_occurance (nums,target):
        l =0
        r = len(nums)-1
        result = -1
        while l <= r:
            mid = l+ (r-l)//2
            if nums[mid] == target:
                result = mid
                r = mid -1
            elif nums[mid]< target:
                l = mid+1
            else:
                r = mid -1

        return result

    def last_occurance (nums,target):
        l =0
        r = len(nums)-1
        result = -1
        while l <= r:
            mid = l+ (r-l)//2
            if nums[mid] == target:
                result = mid
                l = mid+1
            elif nums[mid]< target:
                l = mid+1
            else:
                r = mid -1

        return result
    nums =sorted(nums)
    output =[]
    l = first_occurance(nums,target)
    r = last_occurance(nums,target)

    if  l == -1 : return output

    for i in range(l,r+1):
        output.append(i)
    return output
        

print(targetIndices([1, 2, 5, 2, 3],2))
