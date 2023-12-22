"""Given a sentence (string), return its word count map. Sentence can include punctuation."""
import re


def map_count_word(string):
    map={}
    normalize = "".join([c.lower() if c.isalnum() else " " for c in string])
    normalize = normalize.split()
    for word in normalize:
        map[word] = map.get(word, 0) + 1
    return map

    # word = ""
    # map = {}
    # for char in string:
    #     if char.isalnum():
    #         word += char
    #     elif word:
    #         map[word.lower()] = map.get(word, 0) + 1
    #         word = ""
    # return map
    # # another solution
    # map = {}
    # words = string.split()
    # for word in words:
    #     word = re.sub("[!.,;?]", "", word)
    #     map[word.lower()] = map.get(word, 0) + 1
    # return map


print(map_count_word("Ali, ali is Here!"))
