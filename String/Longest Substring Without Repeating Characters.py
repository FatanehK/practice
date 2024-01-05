"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def lengthOfLongestSubstring(s):
    window = set()
    l = 0
    result = 0
    for r in range(len(s)):
        while s[r] in window:
            window.remove(s[l])
            l += 1
        window.add(s[r])
        result = max(result, r - l + 1)
    return result


print(lengthOfLongestSubstring("bbbbb"))
