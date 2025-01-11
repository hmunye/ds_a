# Time Complexity: O(log n). `haystack` must be ordered
def binary_search(haystack: list[int], needle: int) -> bool:
    start = 0
    end = len(haystack)

    if end == 0:
        return False

    while start < end:
        # Divides then floors
        mid = (start + end) // 2

        if haystack[mid] == needle:
            return True

        if haystack[mid] < needle:
            start = mid + 1

        if haystack[mid] > needle:
            end = mid

    return False


int_list = [0, 1, 2, 3, 4, 5]

print(binary_search(int_list, 5))
print(binary_search(int_list, 3))
print(binary_search(int_list, 2))
print(binary_search([], 2))
print(binary_search(int_list, -1))
print(binary_search(int_list, 7))
