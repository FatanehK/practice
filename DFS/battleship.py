'''um
Topics
Companies
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0'''



def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    rows = len(board)
    cols = len(board[0])

    def dfs(i, j):
        if i >= rows or j >= cols or board[i][j] != 'X':
            return 0
        board[i][j] = "."
        dfs(i+1, j)  # placed horizontally or vertically on board
        dfs(i, j+1)  # placed horizontally or vertically on board

    count = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'X':
                dfs(i, j)
                count += 1
    return count
print(countBattleships( [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))