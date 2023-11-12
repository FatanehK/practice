"""Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length"""


def maxVowels(s: str, k: int) -> int:
    # iterator
    max_count = 0
    Vowel = ["a", "e", "i", "o", "u"]
    for i in range(len(s)):
        count = 0
        for j in range(len(s[i : i + k])):
            if s[i : i + k][j] in Vowel:
                count += 1
        max_count = max(max_count, count)
    return max_count


# sliding window
    count = 0
    l = 0
    res = 0
    for r in range(len(s)):
        if s[r] in Vowel:
            count += 1
        if r - l + 1 > k:
            count -= 1 if s[l] in Vowel else 0
            l += 1
        res = max(res, count)
    return res


print(maxVowels("abciiidef", 3))
