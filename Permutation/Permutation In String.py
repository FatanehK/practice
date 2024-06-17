"""Permutation String
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false"""
from collections import Counter
def checkInclusion(s1: str, s2: str):
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 > len_s2: return False
    s1_count = Counter(s1)
    window_count = Counter(s2[:len_s1])

    if s1_count== window_count:
        return True
    for i in range(len_s1,len_s2):
        window_count[s2[i]]+=1

        window_count[s2[i-len_s1]] -=1
        if window_count[s2[i-len_s1]] == 0:
            del window_count[s2[i - len_s1]]
        if s1_count == window_count:
            return True
    return False
s1 = "abc"
s2 = "lecabee"
# s1 = "a"
# s2 = "ab"
print(checkInclusion(s1, s2))
