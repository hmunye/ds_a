# `Divide and Conquer` is a problem-solving technique where a problem is broken
# into smaller subproblems, each of which is solved independently, and their
# solutions are then combined to solve the overall problem. `Quick Sort` is an
# efficient sorting algorithm based on this approach, where the array is divided
# around a pivot element, with values smaller than the pivot placed on the left
# and larger values on the right. This process is recursively repeated on the
# subarrays, resulting in a sorted array

# Time Complexity: O(n log n) or O(n^2) with bad pivot selection


# A `pivot` is selected from the array elements, and an index is used to traverse
# the array. Elements less than or equal to the pivot are moved to its left,
# while elements greater than the pivot are placed on its right. The left and right
# subarrays (excluding the pivot) are then recursively partitioned, with a new
# pivot chosen for each subarray, continuing the process until the subarrays are
# either empty or contain only one element

# The best choices for selecting a pivot in Quick Sort are the random pivot and
# the median-of-three method. The random pivot involves selecting a random element
# from the array, which helps avoid worst-case scenarios that can arise when the
# array is already sorted or nearly sorted. The median-of-three method selects the
# median of the first, middle, and last elements of the array, ensuring that the
# pivot is more likely to produce balanced partitions


def partition(arr: list[int], start: int, end: int) -> int:
    pivot = arr[end]

    idx = start - 1

    for i in range(start, end):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    idx += 1

    arr[idx], arr[end] = arr[end], arr[idx]

    return idx


def quick_sort(arr: list[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot_idx = partition(arr, start, end)

    quick_sort(arr, start, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, end)


arr = [3, 10, 44, 30, 22, 2, 9, 0]

print("BEFORE: ", arr)

quick_sort(arr, 0, len(arr) - 1)

print("AFTER: ", arr)
