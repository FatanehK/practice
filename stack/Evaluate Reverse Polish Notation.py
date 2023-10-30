def evalRPN(tokens):
    """
        :type tokens: List[str]
        :rtype: int
    """
    stack=[]
    for char in tokens:
        if char == "+":
            stack.append(stack.pop() + stack.pop())
        elif char == "*":
            stack.append(stack.pop() * stack.pop())
        elif char == '-':
            a,b = stack.pop(),stack.pop()
            stack.append(b - a)
        elif char == "/":
            a,b= stack.pop(),stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(char))
    return stack[0]
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))