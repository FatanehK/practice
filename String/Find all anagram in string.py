"""Given two strings s and p, return an array of all the start indices of p's anagrams
in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters."""

from collections import Counter
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    len_s = len(s)
    len_p = len(p)
    if len(p)> len(s): return []
    count_p = Counter(p)
    count_window = Counter(s[:len_p])
    result = []
    if count_window == count_p:
        result.append(0)
    for i in range(len_p,len_s):
        count_window[s[i]]+=1
        count_window[s[i - len_p]]-=1

        if count_window[s[i - len_p]] ==0:
            del count_window[s[i - len_p]]
        if count_window == count_p:
            result.append(i - len_p+1)

    return result
print(findAnagrams("abab", "ab"))
