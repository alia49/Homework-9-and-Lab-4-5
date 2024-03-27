class Solution:
    # Method to find the lowest common ancestor in a binary search tree.
    # The lowest common ancestor is the lowest node in T that has both p and q as descendants.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root  # Start from the root of the tree.
        
        # Traverse the tree starting from the root.
        while current:
            # If both p and q are smaller than root, then LCA lies in left.
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are greater than root, then LCA lies in right.
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # We have found the split point, i.e., the LCA node.
                return current

    # Method to sort an array using Bubble Sort algorithm.
    # It repeatedly swaps the adjacent elements if they are in wrong order.
    def sortArray(self, array):
        n = len(array)  # Get the number of elements in array.
        for i in range(n):
            # Last i elements are already in place.
            for j in range(0, n-i-1):
                # Traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element.
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array  # Return the sorted array.

# Example usage:
solution = Solution()  # Creating an object of the Solution class.
array = [4, 3, 8, 1, 5, 9]  # An unsorted array.
sorted_array = solution.sortArray(array)  # Sorting the array using sortArray method.
print(sorted_array)  # Printing the sorted array.

