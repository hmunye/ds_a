from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Node | None = None
        self.prev: Node | None = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.length: int = 0
        self.__head: Node | None = None
        self.__tail: Node | None = None

    def prepend(self, data: T) -> None:
        node = Node(data)

        self.length += 1

        if not self.__head:
            self.__head = node
            self.__tail = node
            return

        node.next = self.__head
        self.__head.prev = node

        self.__head = node

    def insert_at(self, data: T, idx: int) -> None:
        if idx < 0 or idx > self.length:
            raise IndexError("index out of bounds")

        if idx == 0:
            self.prepend(data)
            return

        if idx == self.length:
            self.append(data)
            return

        self.length += 1

        node = Node(data)

        current_node = self.__head

        for _ in range(idx):
            if not current_node:
                break
            current_node = current_node.next

        current_node.prev.next = node
        node.prev = current_node.prev

        node.next = current_node
        current_node.prev = node

    def append(self, data: T) -> None:
        node = Node(data)

        self.length += 1

        if not self.__tail:
            self.__tail = node
            self.__head = node
            return

        self.__tail.next = node
        node.prev = self.__tail

        self.__tail = node

    def remove(self, data: T) -> T | None:
        if self.length == 0:
            return

        current_node = self.__head

        while current_node:
            if current_node.data == data:
                output = current_node.data

                # So it never goes below 0
                self.length = max(0, self.length - 1)

                if self.length == 0:
                    self.__head = None
                    self.__tail = None
                    return output

                if not current_node.next:
                    current_node.prev.next = None
                    self.__tail = current_node.prev
                    del current_node
                    return output

                if not current_node.prev:
                    current_node.next.prev = None
                    self.__head = current_node.next
                    del current_node
                    return output

                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                del current_node

                return output

            current_node = current_node.next

        return

    def remove_at(self, idx: int) -> T | None:
        if self.length == 0:
            return

        if idx < 0 or idx > self.length:
            raise IndexError("index out of bounds")

        # So it never goes below 0
        self.length = max(0, self.length - 1)

        if idx == 0 and self.__head:
            output = self.__head.data

            if self.__head.next:
                self.__head.next.prev = None
                self.__head = self.__head.next
                return output

            self.__head = None
            self.__tail = None
            return output

        if idx == self.length and self.__tail:
            output = self.__tail.data

            if self.__tail.prev:
                self.__tail.prev.next = None
                self.__tail = self.__tail.prev
                return output

            self.__head = None
            self.__tail = None
            return output

        current_node = self.__head

        for _ in range(idx):
            if not current_node:
                break
            current_node = current_node.next

        output = current_node.data

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        del current_node

        return output

    def get(self, idx: int) -> T | None:
        current_node = self.__head

        for _ in range(idx):
            if not current_node:
                break
            current_node = current_node.next

        return current_node.data if current_node else None

    def __str__(self) -> str:
        msg = f"Length: {self.length} "

        current_node = self.__head

        while current_node:
            msg += f"[{current_node.data}] <-> "
            current_node = current_node.next

        msg += "None\n"
        msg += f"HEAD: {self.__head.data if self.__head else None}\n"
        msg += f"TAIL: {self.__tail.data if self.__tail else None}\n"

        return msg


linked_list = LinkedList()

print(linked_list)

linked_list.append(5)
linked_list.append(7)
linked_list.append(9)

print(linked_list)

assert linked_list.get(2) == 9, "Expected 9 at index 2"
assert linked_list.remove_at(1) == 7, "Expected 7 to be removed at index 1"
assert linked_list.length == 2, "Expected length to be 2"

print(linked_list)

linked_list.append(11)

assert linked_list.remove_at(1) == 9, "Expected 9 to be removed at index 1"
assert linked_list.remove(9) is None, "Expected remove(9) to return None"
assert linked_list.remove_at(0) == 5, "Expected 5 to be removed at index 0"
assert linked_list.remove_at(0) == 11, "Expected 11 to be removed at index 0"
assert linked_list.length == 0, "Expected length to be 0"

print(linked_list)

linked_list.prepend(5)
linked_list.prepend(7)
linked_list.prepend(9)

print(linked_list)

assert linked_list.get(2) == 5, "Expected 5 at index 2 after prepend"
assert linked_list.get(0) == 9, "Expected 9 at index 0 after prepend"
assert linked_list.remove(9) == 9, "Expected 9 to be removed"
assert linked_list.length == 2, "Expected length to be 2 after removal"
assert linked_list.get(0) == 7, "Expected 7 at index 0 after removal of 9"

print("ALL TESTS PASSED!")
