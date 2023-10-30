def partition(arr, low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1


def quicksort(arr,low=0,high=None):
    if high is None:
        high = len(arr)-1

    if low < high:
        pi = partition(arr, low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
print(quicksort([1,3,0,5]))

"quick sort time complxity n(log n)----> worse case o(n^2)"
"memory log n "

# pivot = arr[high]
#   i = low-1
#    for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i+1
# def quicksort(arr, low =0, high =None):
#     if high is None:
#         high = len(arr)-1
#     if low < high:
#         pi = partition(arr, low, high)
#         quicksort(arr, low, pi-1)
#         quicksort(arr, pi+1, high)

#     return arr
