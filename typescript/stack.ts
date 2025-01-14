import { strict as assert } from "node:assert";

type TNode<T> = {
    data: T;
    next?: TNode<T>;
};

class Stack<T> {
    public length: number;
    private head: TNode<T> | undefined;

    constructor() {
        this.length = 0;
        this.head = undefined;
    }

    push(data: T): void {
        const node = { data: data } as TNode<T>;

        if (this.length === 0) {
            this.head = node;
            this.length++;
            return;
        }

        this.length++;

        node.next = this.head;
        this.head = node;
    }

    pop(): T | undefined {
        if (this.length === 0) return;

        this.length = Math.max(0, --this.length);

        const head = this.head;

        if (this.length === 0) {
            this.head = undefined;
            delete head?.next;
            return head?.data;
        }

        this.head = this.head?.next;
        delete head?.next;
        return head?.data;
    }

    peek(): T | undefined {
        return this.head?.data;
    }
}

const stack = new Stack<number>();

stack.push(5);
stack.push(7);
stack.push(9);

assert(stack.pop() === 9, "Expected 9 to be popped");
assert(stack.length === 2, "Expected stack length to be 2");

stack.push(11);
assert(stack.pop() === 11, "Expected 11 to be popped");
assert(stack.pop() === 7, "Expected 7 to be popped");
assert(stack.peek() === 5, "Expected 5 to be on top of the stack");
assert(stack.pop() === 5, "Expected 5 to be popped");
assert(
    stack.pop() === undefined,
    "Expected popping from an empty stack to return undefined",
);

stack.push(69);
assert(stack.peek() === 69, "Expected 69 to be on top of the stack");
assert(stack.length === 1, "Expected stack length to be 1");

console.log("ALL TESTS PASSED!");
