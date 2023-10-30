'''Given two arrays, write a function to compute their intersection. 
Example input: nums1 = [1,2,2,1], nums2 = [2,2]. Output: [2,2].'''

def intersection(nums1,nums2):
    map_nums1={}
    for num in nums1:
        map_nums1[num] = map_nums1.get(num,0)+1

    result = []
    for num2 in nums2:
        if num2 in map_nums1 :
            result.append(num2)
    return result


print(intersection([1, 2, 2, 1],[2, 2]))

