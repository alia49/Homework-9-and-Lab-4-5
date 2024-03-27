public class lab5 {
    // Entry point for the program
    public static void main(String[] args) {
        BST tree = new BST(); // Create a new instance of the binary search tree (BST)
        // Example array of keys to insert into the BST
        int[] array = {1, 22, 1, 4, 5, 6, 8};
        for (int num : array) {
            tree.insert(num); // Insert each key into the BST
        }

        // Print the sorted array by performing an inorder traversal of the BST
        System.out.print("Sorted array: ");
        tree.inorder();
    }

    // Static inner class representing a node in the BST
    static class Node {
        int val; // Value of the node
        Node left, right; // Pointers to the left and right child nodes

        // Constructor for creating a new node with a given value
        public Node(int item) {
            val = item;
            left = right = null;
        }
    }

    // Static inner class for the binary search tree (BST)
    static class BST {
        Node root; // Root node of the BST

        // Constructor for creating an empty BST
        public BST() {
            root = null;
        }

        // Method to insert a new key into the BST
        void insert(int key) {
            root = insertRec(root, key);
        }

        // Recursive method to insert a new key into the BST
        Node insertRec(Node root, int key) {
            // If the tree is empty, create a new node for the root
            if (root == null) {
                root = new Node(key);
                return root;
            }

            // Otherwise, recursively find the correct position for the new key
            if (key < root.val)
                root.left = insertRec(root.left, key); // Insert in the left subtree
            else if (key >= root.val) // Duplicates allowed on the right
                root.right = insertRec(root.right, key); // Insert in the right subtree

            return root; // Return the unchanged root node
        }

        // Method to initiate inorder traversal of the BST
        void inorder() {
            inorderRec(root);
        }

        // Recursive method for inorder traversal, printing the BST in sorted order
        void inorderRec(Node root) {
            if (root != null) {
                inorderRec(root.left); // Traverse the left subtree first
                System.out.print(root.val + " "); // Visit the root node
                inorderRec(root.right); // Traverse the right subtree next
            }
        }
    }
}

