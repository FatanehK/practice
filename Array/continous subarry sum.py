'''Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''


def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # this one is not working
    # curr_sum =nums[0]
    # l=0
    # Flag= False
    # for r in range(1,len(nums)):
    #     curr_sum +=nums[r]
    #     while curr_sum % k == 0:
    #         Flag=True
    #         curr_sum -=nums[l]
    #         l+=1
    # if Flag:
    #     return True 
    # return False

    total= 0
    reminder ={0:-1}
    for i,n in enumerate(nums):
        total+= n
        r = total % k
        if not r in reminder:
            reminder[r]=i
        elif i-reminder[r]> 1:
            return True
    return False

print(checkSubarraySum([5,0,0,0],3))