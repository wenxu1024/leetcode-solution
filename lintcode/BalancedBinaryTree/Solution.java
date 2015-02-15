/*
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
import java.util.*;
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    public boolean isBalanced(TreeNode root) {
        // write your code here
        if (root == null) return true;
        if (!isBalanced(root.left)) return false;
        if (!isBalanced(root.right)) return false;
        if (Math.abs(deepth(root.left) - deepth(root.right)) <= 1) return true;
        else return false;
    }
    
    public int deepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(deepth(root.left), deepth(root.right));
    }

    public static void main(String[] args) {}
}


