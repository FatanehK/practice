def longest_valid_parentheses(s):
    max_len = 0
    stack = [-1]
    l = 0
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len


print(longest_valid_parentheses("()"))
