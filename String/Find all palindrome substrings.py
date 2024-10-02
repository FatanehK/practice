#  Find all palindrome substrings
# Problem Statement: Given a string, find all non-single letter substrings that are palindromes.

# Example:


# An string input of "poppopo" would return "pop", "opo", "oppo", and "poppop".
def palindrom(s):
    result = set()
    for i in range(len(s)):

        # odd
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            subs = s[l : r + 1]
            if len(set(subs)) > 1:
                result.add(s[l : r + 1])
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            subs = s[l : r + 1]
            if len(set(subs)) > 1:
                result.add(s[l : r + 1])
            l -= 1
            r += 1
    return result


print(palindrom("poppopo"))
