"""
We are interested in finding the size of largest group of connected zeroes in a square grid.

The matrix will consist of ones and zeroes. For example:

grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

We notice that there are three groups of zeroes that are connected together. Zeroes are connected left, down, up, or right. They are NOT connected diagonally.

The largest of the three groups is the rectangle containing 6 zeroes in the top left corner. Thus, the size of the largest group is 6.

Write a function that takes in a square grid and returns the size of the largest group of zeroes.
"""


def biggest_group_size(grid):
    def dfs(i, j):
        count = 0
        if i < 0 or i >= len(grid) or j >= len(grid[0]) or j < 0 or grid[i][j] != 0:
            return 0
        count += 1
        grid[i][j] = 2
        count += dfs(i + 1, j)
        count += dfs(i - 1, j)
        count += dfs(i, j + 1)
        count += dfs(i, j - 1)
        return count

    max_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                count = dfs(i, j)
                max_count = max(count, max_count)
    return max_count


print(
    biggest_group_size(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
        ]
    )
)
