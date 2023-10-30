def bruteForce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum
print(bruteForce([4,-1,2,-7,3,4]))


def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

    # maxsum =nums[0]
    # L=0
    # curSum  =0
    # maxL=0
    # maxR =0
    # for R in range(len(nums)):
    #     if curSum< 0:
    #         curSum =0
    #         L = R
    #     curSum += nums[R]
    #     if curSum> maxsum:
    #         maxsum = curSum
    #         maxL=L
    #         maxR= R
    # return nums[maxL:]


print(kadanes([4, -1, 2, -7, 3, 4]))
