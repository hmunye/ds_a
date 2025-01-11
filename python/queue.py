# A `queue` is a data structure that follows the FIFO (First In, First Out)
# principle. Elements are added to the end of the queue (enqueue) and removed
# from the front (dequeue). A queue is implemented using a linked list as the
# underlying data structure for storing its elements

# Enqueue updates the tail by adding a new element, and dequeue pops the head
# by removing the element at the front


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None


class Queue:
    def __init__(self) -> None:
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.length: int = 0

    def enqueue(self, data) -> None:
        new_node = Node(data)

        if not self.__tail:
            self.__tail = new_node
            self.__head = new_node

            self.length += 1
            return

        self.__tail.next = new_node
        self.__tail = new_node

        self.length += 1

    # Returns data of removed node or None
    def dequeue(self):
        if not self.__head:
            return

        current_head = self.__head
        self.__head = self.__head.next

        self.length -= 1

        if self.length == 0:
            self.__tail = None
            self.__head = None

        return current_head.data

    # Returns data of top node (head) or None
    def peak(self):
        return self.__head.data if self.__head else None

    def __str__(self) -> str:
        msg = f"Length {self.length}: "
        current_node = self.__head

        while current_node:
            msg += f"|{current_node.data}| -> "
            current_node = current_node.next

        msg += "END"
        return msg


queue = Queue()

print(queue)

queue.enqueue(3)

print(queue)

queue.enqueue(4)

print(queue)

queue.dequeue()

print(queue)

print(queue.peak())
