def removeInvalidParentheses(s):

    stack =[]
    s = list(s)
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if stack :
                stack.pop()
            else:
                s[i] = ""
    for i in stack:
        s[i]= ""
    return "".join(s)
s ="(((s))(("
output = removeInvalidParentheses(s)
print(output)

