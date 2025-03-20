# B3 P3
from lab3_tree import BinaryTree


def binary_tree_diameter(tree: BinaryTree):
    max_diameter = 0

    def inner(tree):
        nonlocal max_diameter

        if tree == None:
            return 0

        left_node = inner(tree.left)
        right_node = inner(tree.right)

        if max_diameter < left_node + right_node:
            max_diameter = left_node + right_node

        if left_node < right_node:
            return right_node + 1

        else:
            return left_node + 1

    inner(tree)
    return max_diameter


root = BinaryTree(1)
root.left = BinaryTree(3)
root.right = BinaryTree(2)
root.left.left = BinaryTree(7)
root.left.right = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.right.right = BinaryTree(5)
root.left.left.left.left = BinaryTree(9)
root.left.right.right.right = BinaryTree(6)
print(binary_tree_diameter(root))
