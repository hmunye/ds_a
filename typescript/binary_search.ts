function binary_search(haystack: number[], needle: number): boolean {
    let start = 0;
    let end = haystack.length;

    while (start < end) {
        const mid = Math.floor((start + end) / 2);

        if (haystack[mid] === needle) {
            return true;
        }

        if (haystack[mid] < needle) {
            start = mid + 1;
        }

        if (haystack[mid] > needle) {
            end = mid;
        }
    }

    return false;
}

const list = [0, 4, 6, 9, 11, 13, 100, 430];

console.log(binary_search(list, 4));
console.log(binary_search(list, 10));
console.log(binary_search(list, 22));
console.log(binary_search(list, 0));
console.log(binary_search(list, -5));
console.log(binary_search([], 14));
console.log(binary_search(list, 0));
