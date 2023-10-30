def reverseStr( s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    result =""
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

# import re
# def spin_words(strs):
#     result=[]
#     str_split = strs.split()
#     for word in str_split:
#         if len(word) >= 5:
#                 word = re.sub("[.,:;?!]"," ",word)
#                 word= list(word)
#                 for i in range(len(word)//2):
#                     word[i], word[-(i+1)] = word[-(i+1)],word[i]
#                 result.append("".join(word))
#         else:
#             result.append(word)

#     return " ".join(result)
    


# print(spin_words("Hello world, welcome to the galaxy"))