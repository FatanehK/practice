def contains_duplicate(arry):
    arry.sort() #nlogn
    i=1
    while i < len(arry):
        if arry[i] == arry[i-1]:
            return True
        else:
            i+=1
print(contains_duplicate([2,2,0,0,-1,9]))   