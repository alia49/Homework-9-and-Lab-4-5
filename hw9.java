public class hw9{

    // Method to find the lowest common ancestor in a binary search tree
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode current = root;
        while (current != null) {
            if (p.val < current.val && q.val < current.val) {
                current = current.left;
            } else if (p.val > current.val && q.val > current.val) {
                current = current.right;
            } else {
                return current;
            }
        }
        return null; // This line should never be reached if p and q are guaranteed to be in the tree
    }

    // Method to sort an array using Selection Sort algorithm
    public void sortArray(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n-1; i++) {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;

            // Swap the found minimum element with the first element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }

    // Main method to test the sortArray method
    public static void main(String[] args) {
        hw9 solution = new hw9();
        int[] array = {4, 3, 8, 1, 5, 9};
        
        solution.sortArray(array);
        
        // Print the sorted array
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }
}

// TreeNode class definition (assuming it's defined elsewhere in your code)
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) { this.val = val; }
}
