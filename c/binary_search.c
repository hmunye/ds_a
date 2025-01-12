#include <math.h>
#include <stdbool.h>
#include <stdio.h>

bool binary_search(int *haystack, size_t size, int needle) {
    int start = 0;

    while (start < size) {
        int mid = floor((start + size) / 2.0);

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

    printf("%i\n", binary_search(arr, size, 40));
    printf("%i\n", binary_search(arr, size, 0));
    printf("%i\n", binary_search(arr, size, -5));
    printf("%i\n", binary_search(arr, size, 10));
    printf("%i\n", binary_search(arr, size, 50));

    return 0;
}
