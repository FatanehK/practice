"""Count the number of passing car pairs.

Problem Description:

You are given an array A consisting of N integers representing cars traveling in two directions:

0 represents a car traveling east.
1 represents a car traveling west.
Write a function:

Given A = [0, 1, 0, 1, 1], the function should return 5."""


def passing_cars(A):
    east_count = 0
    passing_pairs = 0

    for car in A:
        if car == 0:
            east_count += 1
        elif car == 1:
            passing_pairs += east_count

    return passing_pairs


print(passing_cars([1, 1, 0, 1, 0, 1]))
