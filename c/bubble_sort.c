#include <stdbool.h>
#include <stdio.h>

void bubble_sort(int *unsorted_arr, size_t size) {
    for (size_t i = 0; i < size; ++i) {
        for (size_t j = 0; j < size - i - 1; ++j) {
            if (unsorted_arr[j] > unsorted_arr[j + 1]) {
                unsorted_arr[j] = unsorted_arr[j] ^ unsorted_arr[j + 1];
                unsorted_arr[j + 1] = unsorted_arr[j] ^ unsorted_arr[j + 1];
                unsorted_arr[j] = unsorted_arr[j] ^ unsorted_arr[j + 1];
            }
        }
    }
}

int main(void) {
    int unsorted_arr[] = {0, 4, 2, 50, 14, 44, 30, 12, 7, 2};
    size_t size = sizeof(unsorted_arr) / sizeof(*unsorted_arr);

    printf("[");
    for (size_t i = 0; i < size; ++i) {
        printf("%d,", unsorted_arr[i]);
    }
    printf("]\n");

    bubble_sort(unsorted_arr, size);

    printf("[");
    for (size_t i = 0; i < size; ++i) {
        printf("%d,", unsorted_arr[i]);
    }
    printf("]\n");

    return 0;
}
