def is_mirror_integer(integer):
    original_int = integer

    reverse_int = 0
    while integer > 0:
        digit = integer % 10
        reverse_int = reverse_int * 10 + digit
        integer = integer // 10
    return original_int == reverse_int


print(is_mirror_integer(12321))
