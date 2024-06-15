"""reverses the first k characters for every 2k characters in the string,
leaving the next k characters unchanged, 
and repeats this pattern until the entire string is processed."""

def reverseStr( s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    result = ""
    i =0
    while i < len(s):

        substring = list(s[i:i+k])
        substring.reverse()
        result += "".join(substring)

        result += s[i+k :i+2*k]

        i += 2 * k

    return result


s1 = "abcdefg"
k1 = 2
print(reverseStr(s1, k1))  # Output: "bacdfeg"