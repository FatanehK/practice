def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    map ={}
    string_lis=""
    for char in licensePlate:
        if char.isalpha():
            char = char.lower()
            string_lis +=char
            map[char]= map.get(char,0)+1
    list_word= []
    for word in words:
        for char in word:
            if map.get(char,0)>0:
                map[char]-=1
                continue
            else:
                break
    list_word.append(word)
    result = sorted(list_word)[0]
    return result
        

print(shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
