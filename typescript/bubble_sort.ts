function bubble_sort(unsorted_arr: number[]): void {
    for (let i = 0; i < unsorted_arr.length; ++i) {
        for (let j = 0; j < unsorted_arr.length - i - 1; ++j) {
            if (unsorted_arr[j] > unsorted_arr[j + 1]) {
                unsorted_arr[j] = unsorted_arr[j] ^ unsorted_arr[j + 1];
                unsorted_arr[j + 1] = unsorted_arr[j] ^ unsorted_arr[j + 1];
                unsorted_arr[j] = unsorted_arr[j] ^ unsorted_arr[j + 1];
            }
        }
    }
}

const unsorted_arr = [0, 44, 30, 2, 1, 50, 4, 17, 7];

bubble_sort(unsorted_arr);

console.log(unsorted_arr);
