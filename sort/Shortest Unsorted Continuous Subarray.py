'''Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 '''

def findUnsortedSubarray(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    N= len(nums)
    l= N
    r = 0
    # nums2 = sorted(nums)
    # for i in range(len(nums)):
    #     if nums[i]!= nums2[i]:
    #         l = min(l,i)
    #         r = max(r,i)
    # if l == len(nums):
    #     return 0
    # else:
    #     return (r - l)+ 1

    stack =[]
    # [(i,number)]
    max_num = float('-inf')
    for i, n in enumerate(nums):
        while stack and stack[-1][1] > n:
            num = stack.pop()
            l = min(l, num[0])
            max_num = max(max_num, num[1])
        stack.append((i,n))
    if l == len(nums):
        return 0
    for j in range(N-1,-1,-1):
        if nums[j] < max_num:
            r = j
            break
    return r - l + 1
print(findUnsortedSubarray([2,6,4,8,10,9,15]))