# Subarray Sum Equals K

# Problem: Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals k.


def subarraySum(nums, k):
    curr_sum = 0
    count = 0
    sum_map = {0: 1}  # To handle the case where the subarray starts at the beginning

    for num in nums:
        curr_sum += num

        diff = curr_sum - k
        if diff in sum_map:
            count += sum_map[diff]

        sum_map[curr_sum] = sum_map.get(curr_sum,0)+1
    return count


# Example usage:
nums = [1, 4, 4]
k = 2
print(subarraySum(nums, 8))  # Output: 1
