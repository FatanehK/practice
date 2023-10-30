'''Given a sentence (string), return its word count map. Sentence can include punctuation.'''
import re
def map_count_word(string):
    word = ""
    map={}
    for char in string:
        if char.isalnum():
            word += char
        elif word:
            map[word.lower()]= map.get(word,0)+1
            word = ""
    return map
# another solution
    map = {}
    words = string.split()
    for word in words:
        word = re.sub('[!.,;?]',"",word)
        map[word.lower()] = map.get(word,0)+1
    return map


print(map_count_word("Ali, ali is Here!"))
