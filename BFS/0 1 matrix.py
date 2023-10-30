'''Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:

'''
from collections import deque
def updateMatrix(mat):
    queue = deque()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                queue.append(mat[i][j])
            else:
                mat[i][j] = "#"
    while queue:
        x,y = queue.popleft()
        for row, col in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_row = x + row
            new_col = y + col

            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]) and mat[new_row][new_col] == "#":
                mat[new_row][new_col] = mat[x][y]+1
                queue.append((new_row, new_col))
