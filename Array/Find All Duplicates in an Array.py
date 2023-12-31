'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.'''

class Solutions:
    def findDuplicates(self, nums):
        # result =[]
        # for n in nums:
        #     n = abs(n)
        #     if nums[n-1]>0:
        #         nums[n-1] *= -1
        #     else:
        #         result.append(n)
        # return result

        # You must solve the problem without modifying the array nums and uses only constant extra space.
        slow =0
        fast =0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast =0
        while fast !=slow:
            slow = nums[slow]
            fast =nums[fast]
        return slow
        

sol = Solutions()
print(sol.findDuplicates([1,3,4,2,2]))
