def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))


def fib(n):
    memo = [0, 1]
    if n == 0:
        return [0]
    elif n == 1:
        return memo

    curr = 2
    while curr <= n:
        memo.append(memo[curr - 1] + memo[curr - 2])
        curr += 1
    return memo


print(fib(6))
