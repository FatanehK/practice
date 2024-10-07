def second_greatest_num(nums):
    largest = float("-inf")
    second_num = float("-inf")

    for num in nums:
        if num > largest:
            second_num = largest
            largest = num
        if num > second_num and num != largest:
            second_num = num
    return second_num if second_num != float("-inf") else -1


print(second_greatest_num([1, 2, 3, 5]))
