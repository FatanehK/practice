'''find maximum sum of subarray of legth k within an array'''

def max_sum_subarray(arr,k):
    if k> len(arr) or k <= 0:
        raise ValueError("Invalid value of K")
    
    max_sum = float('-inf')
    current_sum = sum (arr[:k])
    for i in range(k, len(arr)):
        max_sum = max(max_sum, current_sum)
        current_sum += arr[i]- arr[i-k]
    max_sum = max(max_sum, current_sum)
        
    return max_sum


print(max_sum_subarray([9,1,5,1,3,19],3))
