def generate_parenthesis(n):

    # only add open pranthesis if open < n
    # only add closeing pranthesis if closed < open
    # valid open == closed == n
    # stack =[]
    # result =[]

    # def backtracking(open,close):
    #     if open == close == n:
    #         result.append("".join(stack))

    #     if open < n:
    #         stack.append("(")
    #         backtracking(open+1,close)
    #         # when we are done with backtracking we pop the char from the stack to update stack
    #         # the one that we already add it 
    #         stack.pop()

    #     if close < open:
    #         stack.append(")")
    #         backtracking(open, close+1)
    #         stack.pop()

    # backtracking(0,0)
    # return result
    result = []
    def backtracking(open,close,stack,cand):

        if open == close == 0:
            result.append(cand)
            return 

        if open >0 :
            backtracking(open-1, close, stack+1, cand+"(")
        if close > 0 and stack >0 :
            backtracking(open, close-1, stack-1, cand +")")
    backtracking(n,n,0,"")
    return result

print(generate_parenthesis(2))