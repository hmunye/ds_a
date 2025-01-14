# In-order Traversal:


# In in-order traversal, the nodes are visited in the following order:
# 1. Traverse the left subtree.
# 2. Visit the current node.
# 3. Traverse the right subtree.
#
# Example:
#        [A]
#       /   \
#    [B]     [C]
#   /   \      \
# [D]   [E]    [F]
#
# In-order traversal: D, B, E, A, C, F
#
# The left subtree (D, B, E) is visited first, followed by the root node (A),
# and then the right subtree (C, F).

from typing import TypeVar, Generic

T = TypeVar("T")


class BinaryNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.left: BinaryNode[T] | None = None
        self.right: BinaryNode[T] | None = None


def traverse(curr_node: BinaryNode[int] | None, path: list[int]) -> list[int]:
    # Base Case
    if not curr_node:
        return path

    traverse(curr_node.left, path)

    path.append(curr_node.data)

    traverse(curr_node.right, path)

    return path


def in_order_search(head: BinaryNode[int]) -> list[int]:
    return traverse(head, [])


tree = BinaryNode(20)
tree.left = BinaryNode(10)
tree.left.left = BinaryNode(5)
tree.left.left.right = BinaryNode(7)
tree.left.right = BinaryNode(15)

tree.right = BinaryNode(50)
tree.right.left = BinaryNode(30)
tree.right.left.left = BinaryNode(29)
tree.right.left.right = BinaryNode(45)
tree.right.right = BinaryNode(100)

expected = [
    5,
    7,
    10,
    15,
    20,
    29,
    30,
    45,
    50,
    100,
]

result = in_order_search(tree)
assert result == expected, f"Test failed: Expected {expected}, got {result}"

print("TEST PASSED!")
