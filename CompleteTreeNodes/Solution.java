/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int left, right;
        if (isFull(root.left)) {
            left = countFull(root.left);
        }
        else {
            left = countNodes(root.left);
        }
        if (isFull(root.right)) {
            right = countFull(root.right);
        }
        else {
            right = countNodes(root.right);
        }
        return left + right + 1;
    }
    
    public boolean isFull(TreeNode root) {
        int l, r;
        l = 0;
        r = 0;
        TreeNode c = root;
        while(c != null) {
            l += 1;
            c = c.left;
        }
        c = root;
        while(c != null) {
            r += 1;
            c = c.right;
        }
        return (l == r);
    }
    
    public int countFull(TreeNode root) {
        if (root == null) return 0;
        int l = 1;
        TreeNode c = root;
        while(c != null) {
            l <<= 1;
            c = c.left;
        }
        return l - 1;
    }
}
