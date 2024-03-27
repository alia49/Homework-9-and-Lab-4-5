
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

if __name__ == "__main__":
    bst = BST()
    array = [1, 22, 1, 4, 5, 6, 8]
    for num in array:
        bst.insert(num)
    print("Sorted array:", bst.inorder_traversal())
