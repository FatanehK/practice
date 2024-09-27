"""Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique."""

# def subset(nums):
#     result =[]
#     subset=[]

#     def dfs(i):
#         if i>=len(nums):
#             result.append(subset[:])
#             return
#         # descion to include nums[i]
#         subset.append(nums[i])
#         dfs(i+1)


#         #desion to Not include nums[i]
#         subset.pop()
#         dfs(i+1)

#     dfs(0)
#     return result

# print(subset([1,2,3]))


def subset(nums):
    result = []

    def backtrack(start, path, result):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, result)
            path.pop()

    backtrack(0, [], result)
    return result

print(subset([1, 2, 3]))
