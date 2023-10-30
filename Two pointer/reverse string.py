def reverseString(s):
    """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
    """
        # for i in range(0, len(s)//2):
        #     s[i], s[-(i+1)]= s[-(i+1)],s[i]
        # return s

    
    
    s_split= s.split(",")
    result = ""
    for word in s_split:
        i=0
        word= list(word)
        j = len(word)-1
        while i < j:
            word[i],word[j] = word[j],word[i]
            i+=1
            j-=1
        result += "".join(word)
        result +=","
    return "".join(result )
print(reverseString("hello,word"))