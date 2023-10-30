'''Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

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
s and p consist of lowercase English letters.'''


def findAnagrams(s, p):
    """
        :type s: str
        :type p: str
        :rtype: List[int]
    """
    l = 0
    result = []
    if len(p)> len(s):
        return result
    scount ={}
    pcount={}
    for i in range(len(p)):
        pcount[p[i]] = pcount.get(p[i],0)+1
        scount[s[i]]= scount.get(s[i],0)+1
    result = [0] if pcount == scount else []
    for r in range(len(p),len(s)):
        scount[s[r]]= scount.get(s[r],0)+1
        scount[s[l]]-=1

        if scount[s[l]]==0:
            scount.pop(s[l])
        l+=1
        if scount == pcount :
            result.append(l)
    return result
    
print(findAnagrams("a","ab"))