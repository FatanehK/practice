"""You are given an m x n integer matrix matrix with the following two properties:

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

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""


def searchMatrix(matrix, target):
    Rows = len(matrix)
    Cols = len(matrix[0])
    top = 0
    bot = Rows - 1
    while top <= bot:
        mid = (top + bot) // 2
        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bot = mid - 1
        else:
            break
    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, Cols - 1
    while l <= r:
        m = (r + l) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

    # logm + logn


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
