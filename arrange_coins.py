def arrange_coins(n):
    # if n<= 0:
    #     return 0
    # count = 1
    # while n > 0:
    #     n = n-count
    #     if n < 0 :
    #         break
    #     count += 1
    # return count-1
    
    rows = 0
    coins = 0
    while coins + rows + 1 <= n:
        rows += 1
        coins += rows

    return rows


    start=0
    end= n
    while start <= end:
        mid = start+(end-start//2)
        current_sum = mid*(mid+1)//2
        if current_sum == n:
            return mid
        elif current_sum< n:
            start = mid+1
        else:
            end =mid -1
    return start-1

print(arrange_coins(7))
