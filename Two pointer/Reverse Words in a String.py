def reverseWords(s):
    """
        :type s: str
        :rtype: str
        """
    # it need optimization

    i = 0
    split_s= s.split(" ")
    j = len(split_s)-1

    while i < j :
        if split_s[i] == "":
            i+=1
            continue 
        if split_s[j] == "" :
            j-=1
        else:
            split_s[i],split_s[j]= split_s[j],split_s[i]
            i+=1
            j-=1
    revers_string = " ".join(split_s)
    return revers_string


print(reverseWords( "the sky is blue"))
