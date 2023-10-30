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
Output: 8"""

def diagonalSum(mat):
    """
        :type mat: List[List[int]]
        :rtype: int
    """
    sum =0 
    l = len(mat)
    for i in range(l):
        sum += mat[i][i]
        sum +=mat[i][l-1-i]
    if l //2 == 0 or l % 2 == 1:
        sum -= mat[i-l//2][i-l//2]
    return sum

print(diagonalSum([[1,2,3],
            [4,5,6],
            [7,8,9]]))

# l = len(mat)
#   sum = 0
#    for i in range(l):
#         sum += mat[i][i]
#         sum += mat[i][l-1-i]
#     if l %2 == 1 or l//2 == 0:
#         sum -= mat[i-l//2][i-l//2]
#     return sum
