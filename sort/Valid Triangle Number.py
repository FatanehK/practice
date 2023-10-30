'''Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000'''

def valid_triangle_number(nums):

    N = len(nums)
    count = 0
    nums.sort()
    for i in range(2,N):
        l = 0
        r = i-1
        while l < r:
            if nums[l]+nums[r]> nums[i]:
                count += r-l
                r-=1
            else:
                l+=1
    return count

print(valid_triangle_number([2,2,3,4]))