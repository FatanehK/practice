def bubblesort(arry):
    n = len(arry)
    for i in range(n):
        swapped = False
        for j in range (n-i-1):
            if arry[j]> arry[j+1]:
                arry[j], arry[j+1] =arry[j+1],arry[j]
                swapped = True
        if not swapped :
            break
    return arry

print(bubblesort([8,-1,0]))