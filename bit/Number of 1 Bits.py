'''Write an efficient program to count the number of 1s in the binary representation of an integer.
Examples : 

Input : n = 6
Output : 2
Binary representation of 6 is 110 and has 2 set bits

Input : n = 13
Output : 3
Binary representation of 13 is 1101 and has 3 set bits

'''


def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count


# Program to test function countSetBits */
i = 9
print(countSetBits(3))
