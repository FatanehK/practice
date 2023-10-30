"""Given an unsorted array scores (integer) and a highest possible score (integer), return a sorted array."""

'''Function Name: scoreSettler
Input: array of integers representing scores and a single integer for the highest possible score
Output: A sorted array of integers in descending order
Example: scoreSettler([ 1, 2, 3, 999999], 1000000) => [999999, 3, 2, 1]'''



def scoreSettler(array,num):
    return quicksort(array,0,len(array) - 1)


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

    result = []
    while array:
        
        max_score =float('-inf')
        for score in array:
            max_score= max(max_score,score)
        if max_score <= num:
            result.append(max_score)
            array.remove(max_score)
        else:
            array.remove(max_score)
    return result

print(scoreSettler([1, 2, 3, 999999],1000000))

