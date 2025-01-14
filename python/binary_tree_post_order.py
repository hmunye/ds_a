# Post-order Traversal:

# In post-order traversal, the nodes are visited in the following order:
# 1. Traverse the left subtree.
# 2. Traverse the right subtree.
# 3. Visit the current node.
#
# Example:
#        [A]
#       /   \
#    [B]     [C]
#   /   \      \
# [D]   [E]    [F]
#
# Post-order traversal: D, E, B, F, C, A
#
# The left subtree (D, E, B) is visited first, followed by the right subtree (F, C),
# and finally the root node (A).

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class BinaryNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.left: Optional[BinaryNode[T]] = None
        self.right: Optional[BinaryNode[T]] = None


def traverse(curr_node: BinaryNode[int] | None, path: list[int]) -> list[int]:
    # Base Case
    if not curr_node:
        return path

    traverse(curr_node.left, path)

    traverse(curr_node.right, path)

    path.append(curr_node.data)

    return path


def post_order_search(head: BinaryNode[int]) -> list[int]:
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

expected = [7, 5, 15, 10, 29, 45, 30, 100, 50, 20]
result = post_order_search(tree)
assert result == expected, f"Test failed: Expected {expected}, got {result}"

print("TEST PASSED!")
