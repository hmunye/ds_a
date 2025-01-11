# A stack is a linear data structure that follows the Last In, First Out (LIFO)
# principle, meaning that the most recently added element is the first to be
# removed. The main operations associated with a stack are push
# (to add an element), pop (to remove the top element), peek
# (to view the top element without removing it)

import random


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.__head = None
        self.length = 0

    def push(self, data) -> None:
        new_node = Node(data)

        self.length += 1

        if not self.__head:
            self.__head = new_node
            return

        new_node.next = self.__head
        self.__head = new_node

    def pop(self):
        if not self.__head:
            return

        # Either keep it at 0, or decrement if not negative
        self.length = max(0, self.length - 1)

        current_head = self.__head

        if self.length == 0:
            self.__head = None
        else:
            self.__head = current_head.next

        return current_head.data

    def peek(self):
        return self.__head.data if self.__head else None

    def __str__(self) -> str:
        msg = f"Length: {self.length} "

        current_head = self.__head

        while current_head:
            msg += f"[{current_head.data}] -> "
            current_head = current_head.next

        msg += "END"
        return msg


stack = Stack()

print(stack)

stack.push(3)

print(stack)

stack.push(7)

print(stack)

print(f"Removed: {stack.pop()}")

print(stack)

for i in range(0, 5):
    stack.push(int(random.random() * 100))

print(stack)

print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
print(f"Removed: {stack.pop()}")
