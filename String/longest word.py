'''Find the length of the longest word in a sentence.'''

# input = "Rosh is coming from school. "
# output = int 
# return 0
# two same lenghth
import re 
def longest_word(input):
    list_word = input.split()
    print(list_word)
    longest = 0
    for word in list_word:
        # re.sub(pattern)
        word = re.sub('[!.,;?]', '', word)
        lenght = len(word)
        longest = max(longest,lenght)
    return longest


print(longest_word("Rosh is coming from school."))
