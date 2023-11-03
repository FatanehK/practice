def removeInvalidParentheses(s):
    stack = []
    open_count =0
    for char in s:
        if char == '(':
            stack.append(char)
            open_count +=1
        elif char == ')':
            if open_count > 0:
                stack.append(char)
                open_count-=1
        else:
            stack.append(char)
    return "".join(stack)
            

    
s = "))())))"
output = removeInvalidParentheses(s)
print(output)
