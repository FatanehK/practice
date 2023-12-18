"""Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""


def diagonalSum(mat):
    m = len(mat)
    sum = 0
    for i in range(m):
        sum += mat[i][i]
        # if len matrix is odd and i == len(matrix)//2 skip that row
        if m % 2 == 1 and i == m// 2 :
            continue
        sum += mat[i][m - 1 - i]
    return sum


print(diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
