public class lab4 {

    public static void main(String[] args) {
        BST bst = new BST();
        int[] array = {1, 2, 1, 4, 5, 6, 8};
        for (int num : array) {
            bst.insert(num);
        }
        System.out.println("Sorted array: " + bst.inorderTraversal());
    }
}

class Node {
    int val;
    Node left, right;

    public Node(int key) {
        this.val = key;
        this.left = null;
        this.right = null;
    }
}

class BST {
    private Node root;

    public BST() {
        this.root = null;
    }

    public void insert(int key) {
        this.root = insert(this.root, key);
    }

    private Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key);
        }
        if (key < node.val) {
            node.left = insert(node.left, key);
        } else { // Allow duplicates to go to the right subtree
            node.right = insert(node.right, key);
        }
        return node;
    }

    public String inorderTraversal() {
        StringBuilder builder = new StringBuilder();
        inorderTraversal(this.root, builder);
        return builder.toString();
    }

    private void inorderTraversal(Node node, StringBuilder builder) {
        if (node != null) {
            inorderTraversal(node.left, builder);
            builder.append(node.val).append(" ");
            inorderTraversal(node.right, builder);
        }
    }
}
