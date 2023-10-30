def lsf(s,k):
    # left=0
    # max=0
    # while (left+max) < len(s):
    #     uniqueChars = set()
    #     localMax = 0
    #     for i in range(left, len(s)):
    #         uniqueChars.add(s[i])
    #         if len(uniqueChars)>k:
    #             break
    #         localMax+=1
    #     if max<localMax:
    #         max= localMax

    #     left+=1

    # return max

        
        


    # for r, char in enumerate (s):
    #     if char not in window:
    #         window.add(char)
    #     while k < 0:
    #         window.remove(s[l])
    #         l+=1
    #         k+=1
    #     result= max(result,r-l+1)
    # return result 

    # if k == 0:
    #     return 0

    char_map = {}
    max_length = 0
    left = 0

    for r in range(len(s)):
        if s[r] not in char_map:
            char_map[s[r]] = 1
        else:
            char_map[s[r]] += 1

        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1

        max_length = max(max_length, r - left + 1)

    return max_length

print(lsf("ecebaa",2))
    