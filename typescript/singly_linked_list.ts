type TNode<T> = {
    data: T;
    next?: TNode<T>;
};

interface ILinkedList<T> {
    get length(): number;
    insertAt(data: T, idx: number): void;
    remove(data: T): T | undefined;
    removeAt(idx: number): T | undefined;
    append(data: T): void;
    prepend(data: T): void;
    get(idx: number): T | undefined;
    print(): void;
}

class LinkedList<T> implements ILinkedList<T> {
    private head: TNode<T> | undefined;
    private tail: TNode<T> | undefined;
    public length: number;

    constructor() {
        this.head = this.tail = undefined;
        this.length = 0;
    }

    insertAt(data: T, idx: number): void {
        if (idx < 0 || idx > this.length) {
            throw new Error("index out of bounds");
        }

        if (idx === 0) {
            this.prepend(data);
            return;
        }

        if (idx === this.length) {
            this.append(data);
            return;
        }

        const node = { data: data } as TNode<T>;

        if (this.length === 0) {
            this.head = this.tail = node;
            this.length++;
            return;
        }

        this.length++;

        let previous_node: TNode<T> | undefined = undefined;
        let current_node: TNode<T> | undefined = this.head;

        for (let i = 0; i < idx && current_node; ++i) {
            previous_node = current_node;
            current_node = current_node.next;
        }

        previous_node!.next = node;
        node.next = current_node;
    }

    append(data: T): void {
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

    prepend(data: T): void {
        const node = { data: data } as TNode<T>;

        if (this.length === 0) {
            this.head = this.tail = node;
            this.length++;
            return;
        }

        this.length++;

        node.next = this.head;
        this.head = node;
    }

    remove(data: T): T | undefined {
        if (this.length === 0) {
            return;
        }

        if (this.head && this.head.data === data) {
            this.length = Math.max(0, --this.length);

            const rm_node = this.head;

            if (this.length === 0) {
                this.head = this.tail = undefined;

                return rm_node.data;
            }

            this.head = rm_node.next;

            rm_node.next = undefined;

            return rm_node.data;
        }

        let previous_node: TNode<T> | undefined = undefined;
        let current_node: TNode<T> | undefined = this.head;

        while (current_node) {
            if (current_node.data === data) {
                this.length = Math.max(0, --this.length);

                if (this.length === 0) {
                    const rm_node = current_node;

                    this.head = this.tail = undefined;

                    return rm_node.data;
                }

                if (!current_node.next) {
                    const rm_node = current_node;

                    previous_node!.next = undefined;

                    this.tail = previous_node;

                    rm_node.next = undefined;

                    return rm_node.data;
                }

                const rm_node = current_node;

                previous_node!.next = current_node.next;

                rm_node.next = undefined;

                return rm_node.data;
            }

            previous_node = current_node;
            current_node = current_node.next;
        }

        return;
    }

    removeAt(idx: number): T | undefined {
        if (this.length === 0) {
            return;
        }

        if (idx < 0 || idx > this.length) {
            throw new Error("index out of bounds");
        }

        if (this.head && idx === 0) {
            this.length = Math.max(0, --this.length);

            const rm_node = this.head;

            if (this.length === 0) {
                this.head = this.tail = undefined;

                return rm_node.data;
            }

            this.head = rm_node.next;

            rm_node.next = undefined;

            return rm_node.data;
        }

        this.length = Math.max(0, --this.length);

        let previous_node: TNode<T> | undefined = undefined;
        let current_node: TNode<T> | undefined = this.head;

        for (let i = 0; i < idx && current_node; ++i) {
            previous_node = current_node;
            current_node = current_node.next;
        }

        if (this.length === 0) {
            const rm_node = current_node;

            this.head = this.tail = undefined;

            return rm_node?.data;
        }

        // Handle tail removal
        if (current_node && !current_node.next) {
            const rm_node = current_node;

            previous_node!.next = undefined;

            this.tail = previous_node;

            rm_node.next = undefined;

            return rm_node.data;
        }

        const rm_node = current_node;

        previous_node!.next = current_node?.next;

        rm_node!.next = undefined;

        return rm_node?.data;
    }

    get(idx: number): T | undefined {
        if (this.length === 0) {
            return;
        }

        if (idx < 0 || idx > this.length) {
            throw new Error("index out of bounds");
        }

        if (this.head && idx === 0) {
            return this.head.data;
        }

        if (this.tail && idx === this.length) {
            return this.tail.data;
        }

        let previous_node: TNode<T> | undefined = undefined;
        let current_node: TNode<T> | undefined = this.head;

        for (let i = 0; i < idx && current_node; ++i) {
            previous_node = current_node;
            current_node = current_node.next;
        }

        return current_node?.data;
    }

    print(): void {
        let msg = "";

        msg += `Len: ${this.length} `;

        let current_node: TNode<T> | undefined = this.head;

        while (current_node) {
            msg += `[${current_node.data}] -> `;
            current_node = current_node.next;
        }

        msg += "END";
        console.log(msg);
        console.log("HEAD:", this.head ? this.head.data : "undefined");
        console.log("TAIL:", this.tail ? this.tail.data : "undefined");
    }
}

const linked_list = new LinkedList();

linked_list.print();

linked_list.insertAt(10, 0);

linked_list.print();

linked_list.append(20);

linked_list.print();

linked_list.prepend(30);

linked_list.print();

linked_list.insertAt(40, 1);

linked_list.print();

linked_list.insertAt(50, linked_list.length - 1);

linked_list.print();

console.log("Removed:", linked_list.remove(20));

linked_list.print();

console.log("Removed:", linked_list.removeAt(1));

linked_list.print();

console.log("Removed:", linked_list.removeAt(linked_list.length - 1));

linked_list.print();

console.log("Removed:", linked_list.removeAt(0));

linked_list.print();

linked_list.append(30);

linked_list.print();

linked_list.append(40);

linked_list.print();

console.log("Removed:", linked_list.removeAt(0));

linked_list.print();

for (let i = linked_list.length - 1; i >= 0; --i) {
    console.log("Removed:", linked_list.remove(linked_list.get(i)));
    linked_list.print();
}

for (let i = 0; i < 6; ++i) {
    linked_list.insertAt(Math.floor(Math.random() * 100), i);
    linked_list.print();
}

for (let i = 0; i < Math.floor(linked_list.length / 2); ++i) {
    console.log(
        "Removed:",
        linked_list.removeAt(Math.floor(Math.random() * linked_list.length)),
    );
    linked_list.print();
}
