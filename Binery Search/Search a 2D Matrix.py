'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
def search_matrix(matrix,target):
    for i in range(len(matrix)):
        if matrix[i][len(matrix[i])-1] >= target:
            break 

    low =0
    high = len(matrix[i])-1
    while low<= high:
        mid = low + (high-low)//2
        if matrix[i][mid] == target:
            return True
        elif matrix[i][mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False


print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 18))
