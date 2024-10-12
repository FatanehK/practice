"""
Given a non-empty string word and an abbreviation abbr, determine if abbr is a valid abbreviation for word.

Rules:
The abbreviation follows these rules:
A number in abbr represents the number of characters that should be skipped in word.
The numbers cannot have leading zeros.
Every letter and number in abbr should correspond to a character in word."""


def valid_word_abb(word, abb):
    i = 0
    j = 0
    while i < len(word) and j < len(abb):
        if abb[j].isdigit():
            if abb[j] == "0":
                return False
            num = 0
            while j < len(abb) and abb[j].isdigit():
                num = num * 10 + int(abb[j])
                j += 1
            i += num
        else:
            if abb[j] != word[i]:
                return False
            i += 1
            j += 1
    return i == len(word) and j == len(abb)


print(valid_word_abb("internationalization", "i12iz4n"))
