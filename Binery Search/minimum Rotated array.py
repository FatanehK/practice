def min_rotated_sortedarry(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid + 1
    return arr[low]


print(min_rotated_sortedarry([3, 4, 5, 1]))
