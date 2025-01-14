# A `tree` is a hierarchical data structure consisting of `nodes`, where each
# node contains a value and references to child nodes. The topmost node is
# called the `root`, and nodes with no children are called `leaves`. Each node
# can have multiple children, but there is only one parent (except for the root)

# Trees enable efficient searching, insertion, and deletion operations, with
# time complexities typically ranging from O(log n) to O(n) depending on the
# structure's balance

# Nodes in a tree are similar to those in linked lists, where each node contains
# a value and references to its children. The number of children a node has
# indicates its level of connectivity. Children would go in place of a next and/or
# prev reference

# Terminology:
# - root: the topmost node (the parent of all other nodes)

# - height: the length of the longest path from the root to a leaf node

# - binary tree: a tree where each node has at most 2 children, but at least
#                0 children

# - general tree: a tree where each node can have 0 or more children

# - binary search tree: a binary tree with a specific order for nodes,
#                       typically left < parent < right

# - leaves: nodes that do not have any children

# - balanced: a tree is considered `perfectly` balanced when every node's left
#             and right sub-trees have equal height

# - branching factor: the number of children each node can have in the tree

#        [A]
#       /   \
#    [B]     [C]
#   /   \      \
# [D]   [E]    [F]

# Root = A (topmost node)
# Height = 2 ([A] -> [B] -> [D] or [A] -> [C] -> [F])
# Binary Tree = true (each node as at most 2 children)
# General Tree = true (each node has 0 or more children)
# Leaves = D, E, F (nodes without children)
# Balanced = false (for perfect balance, sub-trees must have identical structure and height)
# Branching Factor = 2

# Tree traversal refers to the process of visiting each node in a tree.
# There are different methods for traversing a tree, such as pre-order,
# in-order, and post-order


# Pre-order Traversal:

# In pre-order traversal, the nodes are visited in the following order:
# 1. Visit the current node.
# 2. Traverse the left subtree.
# 3. Traverse the right subtree.
#
# Example:
#        [A]
#       /   \
#    [B]     [C]
#   /   \      \
# [D]   [E]    [F]
#
# Pre-order traversal: A, B, D, E, C, F
#
# The root node (A) is visited first, followed by the left subtree (B, D, E),
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

    path.append(curr_node.data)

    traverse(curr_node.left, path)

    traverse(curr_node.right, path)

    return path


def pre_order_search(head: BinaryNode[int]) -> list[int]:
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
    20,
    10,
    5,
    7,
    15,
    50,
    30,
    29,
    45,
    100,
]

result = pre_order_search(tree)
assert result == expected, f"Test failed: Expected {expected}, got {result}"

print("TEST PASSED!")
