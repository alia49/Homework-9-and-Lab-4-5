class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        else:  # Allow duplicates to go to the right subtree
            node.right = self._insert(node.right, key)
        return node

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        elements = []
        if node:
            elements.extend(self._inorder_traversal(node.left))
            elements.append(node.val)
            elements.extend(self._inorder_traversal(node.right))
        return elements

# Create a BST instance
bst = BST()

# Given array
array = [1, 2, 1, 4, 5, 6, 8]
arrays = [10,22,1,39,8,9,2]
# Insert elements of the array into the BST
for num in array:
    bst.insert(num)

for num in arrays:
    bst.insert(num)
# Perform in-order traversal of the BST to get the sorted elements

sorted_array = bst.inorder_traversal()
sorted_array = bst.inorder_traversal()

print("Sorted array:", sorted_array)
print("Sorted array:", sorted_array)
