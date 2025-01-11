# A `linked list` is a data structure in which elements, called `nodes`, are
# are stored in memory, usually the `heap`, in a sequence where each node
# points to the next node in the list. Linked lists do not store elements in a
# contiguous memory space, like with arrays

# Each `node` contains data and a reference (or pointer) to the next node in
# the list. The last `node` typically has its reference initialized to `None`

# Singly linked lists only contain one reference to the next node, so traversal
# only happens in one direction, from the `head` (first node) to the last node.
# With a doubly linked list, each `node` holds two references, one to the next
# node and one to the previous node, allowing for traversal forwards and backwards

# | Operation                  | Singly Linked List (with Tail Reference)| Singly Linked List (without Tail Reference)| Doubly Linked List (with Tail Reference)| Doubly Linked List (without Tail Reference)|
# |----------------------------|-----------------------------------------|--------------------------------------------|-----------------------------------------|--------------------------------------------|
# | Insertion at Head          | O(1)                                    | O(1)                                       | O(1)                                    | O(1)                                       |
# | Insertion at Tail          | O(1)                                    | O(n)                                       | O(1)                                    | O(n)                                       |
# | Insertion at Specific Position | O(n)                                | O(n)                                       | O(n)                                    | O(n)                                       |
# | Deletion from Head         | O(1)                                    | O(1)                                       | O(1)                                    | O(1)                                       |
# | Deletion from Tail         | O(n)                                    | O(n)                                       | O(1)                                    | O(n)                                       |
# | Deletion from Specific Position| O(n)                                | O(n)                                       | O(n)                                    | O(n)                                       |
# | Indexing (Access by Index) | O(n)                                    | O(n)                                       | O(n)                                    | O(n)                                       |


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.length: int = 0

    def insert_at(self, data, index: int) -> None:
        if index > self.length or index < 0:
            raise IndexError("index out of bounds")

        if index == 0:
            self.prepend(data)
            return

        if index == self.length:
            self.append(data)
            return

        new_node = Node(data)
        previous_node = None
        current_node = self.__head

        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = new_node
        new_node.next = current_node

        self.length += 1

        return

    # Returns data of removed node or None
    def remove(self, data):
        if self.length == 0:
            return

        previous_node = None
        current_node = self.__head

        while current_node:
            if current_node.data == data:
                removed_data = current_node.data

                if not previous_node:
                    self.__head = current_node.next
                else:
                    previous_node.next = current_node.next

                self.length -= 1

                if self.length == 0:
                    self.__head = None
                    self.__tail = None

                return removed_data

            previous_node = current_node
            current_node = current_node.next

        return

    # Returns data of removed node or None
    def remove_at(self, index: int):
        if self.length == 0:
            return

        if index > self.length or index < 0:
            raise IndexError("index out of bounds")

        if index == 0:
            removed_data = self.__head.data
            self.__head = self.__head.next

            self.length -= 1

            if self.length == 0:
                self.__head = None
                self.__tail = None

            return removed_data

        previous_node = None
        current_node = self.__head

        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next

        removed_data = current_node.data

        previous_node.next = current_node.next

        self.length -= 1

        if self.length == 0:
            self.__head = None
            self.__tail = None

        return removed_data

    def append(self, data) -> None:
        new_node = Node(data)

        if self.__tail:
            self.__tail.next = new_node
        else:
            # No `self.__tail` means there are no nodes in the linked list
            self.__head = new_node

        self.__tail = new_node

        self.length += 1

        return

    def prepend(self, data) -> None:
        new_node = Node(data)

        # No `self.__head` means there are no nodes in the linked list
        # Means the new node is the head and tail of the linked list
        if not self.__head:
            self.__tail = new_node

        new_node.next = self.__head
        self.__head = new_node

        self.length += 1

        return

    # Returns data of node at index or None
    def get(self, index):
        if self.length == 0:
            return

        if index > self.length or index < 0:
            raise IndexError("index out of bounds")

        current_node = self.__head

        for _ in range(index):
            current_node = current_node.next

        return current_node.data

    def __str__(self) -> str:
        msg = f"Length {self.length}: "
        current_node = self.__head

        while current_node:
            msg += f"|{current_node.data}| -> "
            current_node = current_node.next

        msg += "END"

        return msg


linked_list = LinkedList()

linked_list.append(10)

print(linked_list)

linked_list.append(13)

print(linked_list)

linked_list.prepend(5)

print(linked_list)

print("Removed: ", linked_list.remove(5))

print(linked_list)

print("Removed: ", linked_list.remove_at(linked_list.length - 1))

print(linked_list)

print("Removed: ", linked_list.remove(13))

linked_list.insert_at(9, 0)

print(linked_list)

linked_list.insert_at(17, 1)

print(linked_list)

linked_list.remove_at(1)

print(linked_list)

linked_list.insert_at(20, 1)

print(linked_list)

linked_list.insert_at(17, 1)

print(linked_list)

# 0-based indexing
print(f"Got: {linked_list.get(3)}")

linked_list.remove(10)
linked_list.remove(20)
linked_list.remove(9)
linked_list.remove(17)

print(linked_list)

print(f"Removed: {linked_list.remove(4)}")
