# Time Complexity: O(n^2)


def bubble_sort(unsorted_array: list[int]):
    for i in range(0, len(unsorted_array)):
        for j in range(0, len(unsorted_array) - i - 1):
            if unsorted_array[j] > unsorted_array[j + 1]:
                unsorted_array[j] = unsorted_array[j] ^ unsorted_array[j + 1]
                unsorted_array[j + 1] = unsorted_array[j] ^ unsorted_array[j + 1]
                unsorted_array[j] = unsorted_array[j] ^ unsorted_array[j + 1]


int_list = [10, 2, 4, 7, 5, 6, 20, 31, 3]

bubble_sort(int_list)

print(int_list)
