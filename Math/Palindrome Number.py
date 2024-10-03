def isPalindrome(x: int) -> bool:
    if x < 0 or (x!=0 and x %10 == 0 ):
        return False
    result =0
    temp= x
    while temp > 0:
        digit = temp%10
        temp = temp // 10
        result = result  * 10 + digit 
    return result == x


print(isPalindrome(10))
