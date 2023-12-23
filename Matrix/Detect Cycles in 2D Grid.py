"""Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

 

Example 1:



Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:



Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:



Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid consists only of lowercase English letters.
"""
# 0 0 0 0
# a b b b
# a b a b
# a b b b

# Given a Matrix tell us if there is cycle in it

# a b a a
# a b a a
# a b a a
# a b a a


# a -> a -> a -> a
# |
# a    b -> b -> b
# |
# a
# m x n


# window (0,0)
# def cyclic_matrix(mat):
#     window = set()

#     def dfs(i, j, startingLetter, prevI, prevJ):
#         nonlocal window
#         if (
#             i < 0
#             or i >= len(mat)
#             or j < 0
#             or j >= len(mat[0])
#             or mat[i][j] != startingLetter
#         ):
#             return False
#         if (i, j) in window:
#             return True
#         window.add((i, j))
#         return (
#             (prevI != i + 1 and dfs(i + 1, j, startingLetter))
#             or (prevI != i - 1 and dfs(i - 1, j, startingLetter))
#             or dfs(i, j + 1, startingLetter)
#             or dfs(i, j - 1, startingLetter)
#         )

#     window = set()
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if (i, j) in window:
#                 continue
#             if dfs(i, j, mat[i][j], 0, 0):
#                 return True
#     return False


def containsCycle(grid) -> bool:
    def dfs(i, j, startingLetter, prevI, prevJ):
        nonlocal window
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[0])
            or grid[i][j] != startingLetter
        ):
            return False
        if (i, j) in window:
            return True
        window.add((i, j))
        return (
            (prevI != i + 1 and dfs(i + 1, j, startingLetter, i, j))
            or (prevI != i - 1 and dfs(i - 1, j, startingLetter, i, j))
            or (prevJ != j + 1 and dfs(i, j + 1, startingLetter, i, j))
            or (prevJ != j - 1 and dfs(i, j - 1, startingLetter, i, j))
        )

    window = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in window:
                continue
            if dfs(i, j, grid[i][j], -1, -1):
                return True
    return False


print(containsCycle([["a", "b", "b"], ["b", "z", "b"], ["b", "b", "b"]]))

# O(m x n)

# O(m x n)
#           o( m^2 x n^2)
