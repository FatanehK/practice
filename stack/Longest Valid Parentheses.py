def longest_valid_paranthesis(s):
    stack =[-1]
    mx_len=0
    for i , char in enumerate(s):
        if char =="(":
            stack.append(i)
        elif char == ")":
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                mx_len = max(mx_len,i-stack[-1])

    return mx_len

print(longest_valid_paranthesis("(()()())"))
