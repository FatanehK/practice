'''Given two integer arrays,  return true if every value in the first array has 
it's corresponding value squared in the second array.'''


def is_squared(arry1,arry2):
    # i = 0 
    # j = 0
    # while i < len(arry1) and j < len(arry2):
    #     square = arry1[i]*arry1[i]
    #     if arry2[j] != square :
    #         return False
    #     i+=1
    #     j+=1
    # return True

    for i in range(len(arry1)):
        square = arry1[i]*arry1[i]
        if arry2[i] != square:
            return False
    return True

print(is_squared([1, 2, 3],[1, 4, 9]))
