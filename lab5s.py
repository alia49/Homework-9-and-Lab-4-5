class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root, left=float('-inf'), right=float('inf')):
        if not root:
            return True
        if not (root.val > left and root.val < right):
            return False
        return (self.isValidBST(root.left, left, root.val) and
                self.isValidBST(root.right, root.val, right))

    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

# Helper function to build the tree from the array
def buildTreeFromArray(arrays):
    solution = Solution()
    root = None
    for val in arrays:
        root = solution.insertIntoBST(root, val)
    return root

# Array given
arrays = [4,3,8,1,5,9,11,10]

# Building the tree
root = buildTreeFromArray(arrays)

# Creating a Solution object to use its methods
solution = Solution()

# Checking if the constructed tree is a valid BST
isValid = solution.isValidBST(root)
print("Is the binary tree a valid BST?", isValid)
