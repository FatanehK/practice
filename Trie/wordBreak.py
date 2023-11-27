'''Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.'''


def build_trie(wordDict):
    trie = {}
    for word in wordDict:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['end'] = True  # Mark the end of a word
    return trie


def word_break(s, wordDict):
    trie_root = build_trie(wordDict)
    n = len(s)

    def dfs(start):
        node = trie_root
        for i in range(start, n):
            char = s[i]
            if char in node:
                node = node[char]
                if 'end' in node and (i == n - 1 or dfs(i + 1)):
                    return True
            else:
                break
        return False
    return dfs(0)


# Example usage
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(word_break(s1, wordDict1))  # Output: True

# s2 = "applepenapple"
# wordDict2 = ["apple", "pen"]
# print(word_break(s2, wordDict2))  # Output: True

# s3 = "catsandog"
# wordDict3 = ["cats", "dog", "sand", "and", "cat"]
# print(word_break(s3, wordDict3))  # Output: False

# Example usage
# s1 = "leetcode"
# wordDict1 = ["leet", "code"]
# print(word_break(s1, wordDict1))  # Output: True

# s2 = "applepenapple"
# wordDict2 = ["apple", "pen"]
# print(word_break(s2, wordDict2))  # Output: True


def word_break(s,wordDict):

    dp= [False]* (len(s)+1)
    dp[len(s)]= True
    for i in range(len(s)-1,-1,-1):
        for word in wordDict:
            if (i+len(word))<= len(s) and s[i:i+len(word)]== word:
                dp[i]= dp[i+len(word)]
            if dp[i]:
                break
    return dp[0]


s2 = "leetcode"
wordDict2 = ["code", "leet"]
print(word_break(s2, wordDict2))  # Output: True
