# `Big O Notation` is a way to categorize an algorithm's time and memory
# requirements based on its input. Meant to generalize the growth of the
# algorithm. Growth is with respect to input

# Helps to make decisions on what data structures and algorithms to use in
# certain scenarios

# Example: This function is O(n) time complexity since it will loop through the
# entire input


def sum_char_codes_linear(n: str) -> int:
    sum: int = 0

    for i in range(len(n)):
        sum += ord(n[i])

    return sum


# Example: This function is still O(n) time complexity and not O(2n) even with
# the two for loops. Constants are dropped, since Big O is meant to describe
# the upper bound of the algorithm (growth), and the constant eventually
# becomes irrelevant


def sum_char_codes_still_linear(n: str) -> int:
    sum: int = 0

    for i in range(len(n)):
        sum += ord(n[i])

    for i in range(len(n)):
        sum += ord(n[i])

    return sum


# Example: This function is STILL O(n) time complexity even with the if block
# potentially resulting in an early return. In Big O, the worst case is often
# mainly considered. Even if the string was just contained "E" and the function
# would return after one iteration, the worst case for this function is still
# iterating over the entire string, so O(n)


def sum_char_codes_worst_case_linear(n: str) -> int:
    sum = 0

    for i in range(len(n)):
        charCode = ord(n[i])

        if charCode == 69:
            return sum

        sum += ord(n[i])

    return sum


# Summary:
# - Growth is with respect to the input for the algorithm
# - Constants are always dropped
# - Worst-case is usually the way to measure


# Common Complexities:
# - O(1): Constant Time
def sum_char_codes_constant(n: str) -> str:
    return n


# - O(log n): Logarithmic Time
# (For every iteration, half the input to search, look at one value at a time)
# -- Binary Search / Binary Search Trees

# - O(n): Linear Time


def sum_char_codes_linear_(n: str) -> int:
    sum = 0

    for i in range(len(n)):
        sum += ord(n[i])

    return sum


# - O(n log n): "Linearithmic" time
# (For every iteration, half the input to search, search the halve n times)
# -- Quick Sort


# - O (n^2): Quadratic Time
def sum_char_codes_quadratic(n: str) -> int:
    sum = 0

    for i in range(len(n)):
        for i in range(len(n)):
            sum += ord(n[i])

    return sum


# - O(n^3): Cubic Time
def sum_char_codes_cubic(n: str) -> int:
    sum = 0

    for i in range(len(n)):
        for i in range(len(n)):
            for i in range(len(n)):
                sum += ord(n[i])

    return sum


# - O(2^n): Exponential Time
# --- Subset Sum Problem

# - O(n!): Factorial Time
# --- Traveling Salesman Problem

# - O(sqrt(n)): Square Root Time
# --- Two Crystal Ball Problem
