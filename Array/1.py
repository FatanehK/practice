'''Given an array of integers, return the greatest three.'''


def greatest_three(Array):

    # return sorted(Array, reverse=True)[:3]

    first_max = float('-inf')
    secod_max = float('-inf')
    third_max = float('-inf')
    for num in Array:
        if num > first_max :
            third_max = secod_max
            secod_max = first_max
            first_max = num
        elif num > secod_max and num!= first_max:
            third_max = secod_max
            secod_max = num
        elif num> third_max and num!= first_max and num!= secod_max:
            third_max = num
    return [first_max, secod_max,third_max]
        

print(greatest_three([10, 5, 20, 30, 15]))



