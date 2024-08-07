'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length'''


def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    l =0 
    max_freq =0
    max_len= 0
    map ={}

    for r in range(len(s)):
        map[s[r]] = map.get(s[r],0)+1
        max_freq = max(max_freq,map[s[r]])

        while max_freq+ k < r-l +1:
            map[s[l]]-=1
            if map[s[l]]== 0:
                del map[s[l]]
            l+=1
        max_len = max(max_len,r-l+1)
    return max_len

    # left = 0
    # right = 0
    # result = 0
    # map ={}
    # for right in range(len(s)):
    #     if s[right] not in map:
    #         map[s[right]] =1
    #     else:
    #         map[s[right]]+=1
    #     while (right-left +1) - max(map.values()) > k :
    #         map[s[left]]-=1
    #         left += 1

    #     result = max(result, right-left +1)

    # return result


print(characterReplacement("ABAB", 2))
