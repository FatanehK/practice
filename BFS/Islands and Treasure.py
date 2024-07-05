"""

Islands and Treasure
You are given a m*n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
341256

"""

from collections import deque


def islandsAndTreasure(grid):
    visit = set()
    q = deque()

    def add_cell(r, c):
        if (
            r < 0
            or c < 0
            or r == len(grid)
            or c == len(grid[0])
            or (r, c) in visit
            or grid[r][c] == -1
        ):
            return
        q.append([r, c])
        visit.add((r, c))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                visit.add((r, c))
                q.append([r, c])

    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            if grid[r][c] != 0:  
                grid[r][c] = dist
            add_cell(r + 1, c)
            add_cell(r - 1, c)
            add_cell(r, c + 1)
            add_cell(r, c - 1)
        dist += 1

    return grid



grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

print(islandsAndTreasure(grid))
