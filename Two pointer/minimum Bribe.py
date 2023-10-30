def minimum_bribes(q):
    bribes = 0
    too_chaotic = False

    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            too_chaotic = True
            break

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    if too_chaotic:
        print("Too chaotic")
    else:
        print(bribes)


# Example usage:
queue1 = [2, 1, 5, 3, 4]
minimum_bribes(queue1)  # Output: 3

# queue2 = [2, 5, 1, 3, 4]
# minimum_bribes(queue2)  # Output: Too chaotic
