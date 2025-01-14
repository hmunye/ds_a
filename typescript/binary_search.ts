function binary_search(haystack: number[], needle: number): boolean {
    let lo = 0;
    let hi = haystack.length;

    while (lo < hi) {
        const mid = Math.floor(lo + (hi - lo) / 2);

        if (haystack[mid] === needle) {
            return true;
        }

        if (haystack[mid] < needle) {
            lo = mid + 1;
        }

        if (haystack[mid] > needle) {
            hi = mid;
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
console.log(binary_search(list, 430));
