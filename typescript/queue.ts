import { strict as assert } from "node:assert";

type TNode<T> = {
    data: T;
    next?: TNode<T>;
};

class Queue<T> {
    public length: number;
    private head: TNode<T> | undefined;
    private tail: TNode<T> | undefined;

    constructor() {
        this.length = 0;
        this.head = this.tail = undefined;
    }

    enqueue(data: T): void {
        const node = { data: data } as TNode<T>;

        if (this.length === 0) {
            this.head = this.tail = node;
            this.length++;
            return;
        }

        this.length++;

        this.tail!.next = node;
        this.tail = node;
    }

    deque(): T | undefined {
        if (this.length === 0) return;

        this.length = Math.max(0, --this.length);

        const head = this.head;

        if (this.length === 0) {
            this.head = this.tail = undefined;
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

const queue = new Queue<number>();

queue.enqueue(5);
queue.enqueue(7);
queue.enqueue(9);

assert(queue.deque() === 5, "Expected 5 to be dequeued");
assert(queue.length === 2, "Expected queue length to be 2");

queue.enqueue(11);
assert(queue.deque() === 7, "Expected 7 to be dequeued");
assert(queue.deque() === 9, "Expected 9 to be dequeued");
assert(queue.peek() === 11, "Expected 11 to be at the front of the queue");
assert(queue.deque() === 11, "Expected 11 to be dequeued");
assert(
    queue.deque() === undefined,
    "Expected dequeuing an empty queue to return undefined",
);
assert(queue.length === 0, "Expected queue length to be 0");

queue.enqueue(69);
assert(queue.peek() === 69, "Expected 69 to be at the front of the queue");
assert(queue.length === 1, "Expected queue length to be 1");

console.log("ALL TESTS PASSED!");
