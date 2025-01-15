#include <stdbool.h>
#include <stdio.h>

bool linear_search(int *haystack, size_t size, int needle) {
    for (size_t i = 0; i < size; ++i) {
        if (haystack[i] == needle) {
            return true;
        }
    }

    return false;
}

int main(void) {
    int arr[] = {1, 3, 5, 10, 3, 2, 7};

    size_t size = sizeof(arr) / sizeof(*arr);

    printf("%d\n", linear_search(arr, size, 5));
    printf("%d\n", linear_search(arr, size, 10));
    printf("%d\n", linear_search(arr, size, 7));
    printf("%d\n", linear_search(arr, size, -3));

    return 0;
}
