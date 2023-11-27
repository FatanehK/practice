def canBeEqual(target, arr) -> bool:
    map_t = {}
    map_a = {}
    for num in target:
        map_t[num] = map_t.get(num, 0) + 1
    for num1 in arr:
        map_a[num1] = map_a.get(num1, 0) + 1

    return True


print(canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
