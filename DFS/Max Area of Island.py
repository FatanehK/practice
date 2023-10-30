def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def dfs(grid, i, j):
        count=0
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != 1:
            return 0
        count+=1
        grid[i][j] = "*"
        count += dfs(grid, i+1, j)
        count += dfs(grid, i-1, j)
        count += dfs(grid, i, j+1)
        count += dfs(grid, i, j-1)
        return count

    max_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                x= dfs(grid, i, j)
                max_count = max(max_count, x)

    return max_count
print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))