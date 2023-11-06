'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]'''


def setZeroes(matrix):
    """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
    """
    set_row = set()
    set_col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                set_row.add(i)
                set_col.add(j)

    for i in range(len(matrix)):
        if i in set_row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    for j in range(len(matrix[0])):
        if j in set_col:
            for i in range(len(matrix)):
                matrix[i][j] = 0

    return matrix


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
