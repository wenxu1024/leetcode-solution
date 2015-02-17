import java.util.*;
//Remove Node in binary search tree

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param value: Remove the node with given value.
     * @return: The root of the binary search tree after removal.
     */
    public TreeNode removeNode(TreeNode root, int value) {
        // write your code here
        if (root == null) return null;
        if (root.val == value) return removeNodeHelper(root);
        else if (root.val > value) {
            root.left = removeNode(root.left, value);
            return root;
        }
        else {
            root.right = removeNode(root.right, value);
            return root;
        }
    }
    
    
    
    public TreeNode removeNodeHelper(TreeNode root) {
        if (root == null) return null;
        if (root.left == null && root.right == null) return null;
        else if (root.left != null && root.right == null) return root.left;
        else if (root.left == null && root.right != null) return root.right;
        else {
            TreeNode parent, rchild;
            parent = root.left;
            rchild = parent.right;
            if (rchild == null) {
                root.val = parent.val;
                root.left = parent.left;
                return root;
            }
            else {
                while (rchild.right != null) {
                    parent = rchild;
                    rchild = rchild.right;
                }
                root.val = rchild.val;
                parent.right = rchild.left;
                return root;
            }
        }
    }
};


