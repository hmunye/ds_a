# An `array` is a contiguous memory space of a certain amount of bytes

# Memory is interpreted by the compiler/interpreter based on the data type
# associated with the allocated memory (needs to be given meaning)

import array

# Here, the memory allocated for the array will be interpreted as a sequence
# of `signed int` values, signified by the typecode "i"

# Creates an array of 5 elements, initialized to 0s
arr: array.ArrayType = array.array("i", [0] * 5)

print(arr)  # -> array('i', [0, 0, 0, 0, 0])


# In lower-level languages like C, accessing or modifying an array element
# involves calculating the correct memory address using the base address, the
# offset (index), and the width of the data type in that memory space

# Ex. base address of array + (index * width of type)

arr[0] = 23

print(arr)

# Python abstracts away the memory management from the user
