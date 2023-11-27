"""Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


class TrieNode:
    def __init__(self):
        self.childern = {}
        self.isword = False

    def addword(self, word):
        curr = self
        for c in word:
            if c not in curr.childern:
                curr.childern[c] = TrieNode()
            curr = curr.childern[c]
        curr.isword = True


class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addword(w)
        rows = len(board)
        cols = len(board[0])
        result = set()
        visit = set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or (r, c) in visit
                or board[r][c] not in node.childern
            ):
                return
            visit.add((r, c))
            node = node.childern[board[r][c]]
            word += board[r][c]
            if node.isword:
                result.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(result)

sol= Solution()
print(
    sol.findWords([
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ],["oath", "pea", "eat", "rain"])
)
