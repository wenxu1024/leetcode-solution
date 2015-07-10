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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == p || root == q) return root;
        else {
            if (containsNode(root.left, p) && containsNode(root.right, q) || containsNode(root.right, p) && containsNode(root.left, q)) {
                return root;
            }
            else if (containsNode(root.left, p) && containsNode(root.left, q)) {
                return lowestCommonAncestor(root.left, p, q);
            }
            else {
                return lowestCommonAncestor(root.right, p, q);
            }
            }
    }
    
    
    public boolean containsNode(TreeNode root, TreeNode t) {
        if (root == null) return false;
        else {
            if (root == t) return true;
            else {
                return containsNode(root.left, t) || containsNode(root.right, t);
            }
        }
    }
}
