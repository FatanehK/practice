'''Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

Accepted
1.4M
'''

def longest_increasing_subsequence(nums):
    result =[1]* len(arr)

    for i in range(len(arr)-1,-1,-1):
        for j in range(i+1, len(arr)):
            if arr[i]< arr[j]:
                result[i]= max(result[i],1+result[j])
    return max(result)
    

    # the otherway
    if not nums:
        return 0
    n = len(nums)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

print(longest_increasing_subsequence([1,4,2,3]))
