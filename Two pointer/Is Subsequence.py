def isSubsequence(s, t):
    """
        :type s: str
        :type t: str
        :rtype: bool
    """
    i = len(s)-1
    j = len(t)-1
    if len(s)== 0:
        return True
    while i < j:
        if s[i] == t[j]:
            i-=1
            j-=1
        elif s[i] != t[j]:
            j-=1
    return i == len(s)


print(isSubsequence("abc", "ahbgdc"))
