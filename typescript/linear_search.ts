function linear_search(haystack: number[], needle: number): boolean {
    for (let i = 0; i < haystack.length; ++i) {
        if (haystack[i] === needle) {
            return true;
        }
    }
    return false;
}

const list = [1, 3, 5, 6, 9, 10, 44, 2];

console.log(linear_search(list, 5))
console.log(linear_search(list, 10))
console.log(linear_search(list, 0))
console.log(linear_search(list, -11))
console.log(linear_search([], -11))
