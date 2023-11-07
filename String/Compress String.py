'''
Given a string, such as aabccca, compress the string, such as a2b1c3a1

assumptions:
string has only alpha characters, all lowercase
valid input

Example I/O

input: 'rrttylr'
output: 'r2t2y1l1r1'

input:'rrrsrrrss'
output: 'r3s1r3s2'

input: 'rrtrr'
output: 'r2t1r2'
'''

def compress_string(string):
    start= string[0]
    count=0
    result =[]
    for char in string :
        if char == start:
            count+=1
            continue
        else:
            result.append(start+str(count))
            start = char
            count = 1
    result.append(start+str(count))
    return "".join(result)


print(compress_string('rrtrr'))