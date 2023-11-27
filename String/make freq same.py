def same_frequency(s):
    # map = {}
    # for char in s:
    #     map[char] = map.get(char, 0) + 1
    # min_value = min(map.values())
    # result = []
    # s = list(s)
    # for char in s:
    #     if map[char] > min_value:
    #         map[char] -= 1
    #     elif map[char] == min_value:
    #         result.append(char)
    # return "".join(result)

    map = {}
    min_freq = float("inf")
    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    min_freq = min(map.values())
    result = 0
    for value in map.values():
        if value > min_freq:
            result += (value - min_freq)
    return result
    


print(same_frequency("bbyycccc"))
"abbcc"
