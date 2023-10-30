'''You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:

'''


def numEnclaves(grid) -> int:
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):

        if r < 0 or c < 0 or r == rows or c == cols or not grid[r][c]:
            return
        grid[r][c] = 0
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and grid[r][c] == 1:
                dfs(r, c)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
    return count

    # def dfs(r, c):
        
    #     if r <= 0 or r >= rows or c <= 0 or c == cols-1 or r == rows-1 or c >= cols or grid[r][c] != 1:
    #         return 0
    #     if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
    #         return float('inf')  # Return infinity for boundary cells
    #     grid[r][c] = "*"
    #     count =1
        
    #     count += dfs(r+1, c)
    #     count += dfs(r-1, c)
    #     count += dfs(r, c+1)
    #     count += dfs(r, c-1)
    #     return count
    # rows = len(grid)
    # cols = len(grid[0])

    # result=0
    # for r in range(rows):
    #     for c in range(cols):
    #         if grid[r][c] == 1:
    #             result += dfs(r, c)


    # return result
print(numEnclaves([[0,1,1,0],[0,0,1,0],[0,1,0,0],[0,0,0,0]]))