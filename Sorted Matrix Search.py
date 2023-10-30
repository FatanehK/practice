def Sorted_Matrix_Search(matrix,v):

    if not matrix and not matrix[0]:
        return False
    if v < matrix[0][0]or v> matrix[-1][-1]:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    left =0 
    right = rows * cols -1
    while left <= right:
        mid = left +(right-left)//2
        mid_elemnet = matrix[mid//cols][mid%cols]

        if mid_elemnet == v:
            return True
        elif mid_elemnet< v:
            left= mid +1
        else:
            right = mid-1



print(Sorted_Matrix_Search([[1, 2, 3], [4, 5, 6], [7, 8, 9]],8))
