"""Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"""
def defoding_string(s):
    if len(s) == 1:
            return s

    stack = []
    curr_token = ""
    curr_number = 0
    
    i = 0
    
    while i < len(s):
        
        if s[i].isdigit():
            curr_number = curr_number*10 + int(s[i])
            
        elif s[i] == "[":
            stack.append((curr_number, curr_token))
            curr_number = 0
            curr_token = ""
            
        elif s[i] == "]":
            prev_number, prev_token = stack.pop()
            curr_token = prev_token + curr_token * prev_number
        
        else:
            curr_token += s[i]
        
        i += 1
    
    return curr_token

    # curr_num=0
    # stack =[]
    # curr_token =""
    # i =0
    # while i< len(s):
    #     if s[i].isdigit ():
    #         curr_num = curr_num * 10 +int(s[i])
    #     elif s[i] == "[":
    #         stack.append((curr_num, curr_token))
    #         curr_num=0
    #         curr_token = ""
    #     elif s[i] == "]":
    #         prv_num, pre_token = stack.pop()
    #         curr_token = curr_token + pre_token * prv_num

    #     else:
    #         curr_token+= s[i]
    #     i+=1
    # return curr_token


print(defoding_string("3[a2[c]]"))
