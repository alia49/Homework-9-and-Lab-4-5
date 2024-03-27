class N
# Define a class for a node in the binary search tree (BST).
class Node:
    def __init__(self, key):
        self.val = key  # The value of the node.
        self.left = None  # Reference to the left child node.
        self.right = None  # Reference to the right child node.

# Define a class for the binary search tree.
class BST:
    def __init__(self):
        self.root = None  # Initialize the root of the BST to None.

    # Public method to insert a new key into the BST.
    def insert(self, key):
        # Call the private _insert method starting from the root.
        self.root = self._insert(self.root, key)

    # Private method to insert a new key into the BST, used recursively.
    def _insert(self, node, key):
        # If current node is None, create a new Node with the key.
        if node is None:
            return Node(key)
        elif key < node.val:
            # If key is less than node's value, insert it into the left subtree.
            node.left = self._insert(node.left, key)
        else:  # Allow duplicates to go to the right subtree.
            # If key is greater than or equal to node's value, insert it into the right subtree.
            node.right = self._insert(node.right, key)
        return node  # Return the (possibly updated) node.

    # Public method to perform inorder traversal of the BST.
    def inorder_traversal(self):
        # Call the private _inorder_traversal method starting from the root.
        return self._inorder_traversal(self.root)

    # Private method to recursively perform an inorder traversal of a subtree.
    def _inorder_traversal(self, node):
        elements = []  # Initialize an empty list to hold the elements in sorted order.
        if node:
            # Recursively traverse the left subtree and add its elements.
            elements.extend(self._inorder_traversal(node.left))
            # Add the current node's value.
            elements.append(node.val)
            # Recursively traverse the right subtree and add its elements.
            elements.extend(self._inorder_traversal(node.right))
        return elements  # Return the list of elements in sorted order.
# Create a BST instance

bst = BST()

# Given array
array = [1, 2, 1, 4, 5, 6, 8]
# Insert elements of the array into the BST
for num in array:
    bst.insert(num)

# Perform in-order traversal of the BST to get the sorted elements

sorted_array = bst.inorder_traversal()

print("Sorted array:", sorted_array)
