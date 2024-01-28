"""Given a string and integer k, return the kth non-repeating character 
(example input: "icecream", 2;    ouput: "r" """


def non_repeating_kth_char(s, k):
    map_char = {}
    for char in s:
        map_char[char] = map_char.get(char, 0) + 1
    k_count = 0
    for char in s:
        if map_char[char] == 1:
            k_count += 1
        if k_count == k:
            return char


print(non_repeating_kth_char("icecream", 2))
