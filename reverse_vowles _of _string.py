
def reverseVowels(p):
    """
    :type s: str
    :rtype: str

    """

    vowles = {'a', 'e', 'i', 'o', 'u'}
    s= list(p)
    i = 0
    j = len(s)-1
    
    while i <= j:
        if s[i] in vowles:
            if s[j] in vowles:
                s[i],s[j]= s[j],s[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    return "".join(s)


print(reverseVowels("helo"))
