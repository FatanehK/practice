'''Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

'''


def exist(board, word) -> bool:
    row = len(board)
    col = len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (i < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[i] or (r, c) in path):
            return False
        path.add((r, c))
        result = dfs(r+1, c, i+1) or dfs(r-1, c, i +
                        1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
        path.remove((r, c))
        return result

    for r in range(row):
        for c in range(col):
            if dfs(r, c, 0):
                return True
    return False

# O(n * m * 4^n)
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEO"))