'''You are given two sorted arrays, A and B, where A has a large enough buffer at the end to
hold B. Write a method to merge B into A in sorted order.'''

# Example usage:
A = [1, 3, 5, 0, 0, 0]
B = [2, 4, 6]

def merge_sorted_arrays(A, B):
    m = len(A) - len(B)
    n = len(B)
    i = m -1
    j = n-1
    k = m + n -1

    while i >= 0 and j >= 0 :
        if A[i] > B [j]:
            A[k] = A[i]
            i -=1
        else:
            A[k] =  B [j]
            j -=1
        k -=1
    while j >=0:
        A[k] = B[j]
        k -=1