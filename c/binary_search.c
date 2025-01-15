#include <math.h>
#include <stdbool.h>
#include <stdio.h>

bool binary_search(int *haystack, size_t size, int needle) {
    size_t start = 0;

    while (start < size) {
        int mid = floor(start + (size - start) / 2.0);

        if (haystack[mid] == needle) {
            return true;
        }

        if (haystack[mid] < needle) {
            start = mid + 1;
        }

        if (haystack[mid] > needle) {
            size = mid;
        }
    }

    return false;
}

int main(void) {
    int arr[] = {0, 4, 5, 6, 9, 10, 13, 30, 44, 45};
    size_t size = sizeof(arr) / sizeof(*arr);

    // 0 represents false, 1 represents true
    printf("%i\n", binary_search(arr, size, 40)); // 0
    printf("%i\n", binary_search(arr, size, 0));  // 1
    printf("%i\n", binary_search(arr, size, -5)); // 0
    printf("%i\n", binary_search(arr, size, 10)); // 1
    printf("%i\n", binary_search(arr, size, 50)); // 0

    return 0;
}
