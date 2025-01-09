def linear_search(haystack: list[int], needle: int) -> bool:
    for elem in haystack:
        if elem == needle:
            return True

    return False


int_list = [0, 1, 2, 3, 4, 5]

print(linear_search(int_list, 0))
print(linear_search(int_list, 2))
print(linear_search(int_list, -5))
print(linear_search(int_list, 10))
