# Time Complexity: O(sqrt(n))

"""
Problem:

Given two crystal balls that will break if dropped from a high enough
distance, determine the exact spit in which it will break in the most
optimized way

"""

# We can think of this as an array with True and False values representing
# if the crystal ball has broken

# [False, False, False, False, False, False, False, True, True, .....]

# It is False (crystal ball has not broken), until it is True (crystal ball breaks),
# then it will continue to be True

# We need to determine the most efficient way of finding the first True value
# (first point at which the crystal ball breaks)

# Since this is an ordered array, we can use binary search and search through
# the array O(log n), but when we find our first True value, we must look back
# in the array linearly, O(n), to determine whether it was the actual first break

# Instead of searching by half of `n` (array size), we can instead walk the array
# by the sqrt(n), avoiding the need for searching linearly

import math


def two_crystal_balls(breaks: list[bool]) -> int:
    length = len(breaks)

    if not length:
        return -1

    # We want to walk the array by sqrt(n)
    jmp_unit = math.floor(math.sqrt(length))

    # Keep track of how many units jumped
    step = jmp_unit

    for i in range(0, length, jmp_unit):
        # Found our first break
        if breaks[i]:
            break

        step += jmp_unit

    # Walk one unit back to determine the first break
    for i in range(step - jmp_unit, min(step, length)):
        if breaks[i]:
            # Index of first break
            return i

    return -1


print(two_crystal_balls([False, False, False, False, True, True, True]))
print(two_crystal_balls([]))
print(two_crystal_balls([False, False, False, False]))
print(two_crystal_balls([True, True, True]))
