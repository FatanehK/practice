def spin_words(sentence):
    array = sentence.split()
    output = []
    for item in array:
        if len(item) < 5:
            output.append(item)
        else:
            reverse = item[-1] + item[1:-1][::-1] + item[0]
            output.append(reverse)
    return " ".join(output)
print(spin_words("Hello world, welcome to the galaxy"))


# def fake_bin(x):
#     x_list = list(x)
    
#     result = []
#     for item in x_list:
#         if int(item) < 5:
#             result.append("0")
#         else:
#             result.append("1")
    
#     return "".join(result)
# print(fake_bin("45385593107843568"))







def coin_chain(coins,amount):
    dp =[float('inf')for _ in range(amount+1)]
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    if dp[-1] == float('inf'):
        return -1
    else:
        return dp[-1]


print(coin_chain([1, 2, 5], 11))
# coins = [1,2,5], amount = 11
