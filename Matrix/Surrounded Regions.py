"""Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'."""


def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """

    def dfs(i, j, board):
        if (
            i >= len(board)
            or j >= len(board[0])
            or i < 0
            or j < 0
            or board[i][j] != "O"
        ):
            return False
        board[i][j] = "A"  # Change the marker to 'A'
        dfs(i + 1, j, board)
        dfs(i - 1, j, board)
        dfs(i, j - 1, board)
        dfs(i, j + 1, board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O" and (
                i == len(board) - 1 or j == len(board[0]) - 1 or i == 0 or j == 0
            ):
                dfs(i, j, board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "A":
                board[i][j] = "O"  # Change 'A' back to 'O'

    return board


print(
    solve(
        [
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
)
# print(
#     solve(
#         [
#             ["X", "O", "X", "O", "X", "O"],
#             ["O", "X", "O", "X", "O", "X"],
#             ["X", "O", "X", "O", "X", "O"],
#             ["O", "X", "O", "X", "O", "X"],
#         ]
#     )
# )
