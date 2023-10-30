'''Merge two sorted arrays. Example input: [1, 3, 6], [2, 4]. Output: [1, 2, 3, 4, 6].'''
def Merge(arr1,arr2):

    i = 0
    result =[]
    j =0
    while i< len(arr1)and j< len(arr2):
        if arr1[i]== arr2[j]:
            result.append(arr1[i])
            result.append(arr2[j])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j+=1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i+=1
    return result


print(Merge([1, 3, 6], [2, 4]))
