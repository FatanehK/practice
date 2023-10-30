'''Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


def longestSubstring(s: str, k: int) -> int:
    map = {}
    if len(s) < 0:
        return 0
    for r in range(len(s)):
        if s[r] not in map:
            map[s[r]] = 1
        else:
            map[s[r]] += 1
    for i, char in enumerate(s):
        if map[char] < k:
            left = longestSubstring(s[:i], k)
            right = longestSubstring(s[i+1:], k)

            return max(left, right)

    return len(s)


print(longestSubstring("abbb", 3))
