import java.util.*;

// Binary Search Tree Iterator

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
 * Example of iterate a tree:
 * Solution iterator = new Solution(root);
 * while (iterator.hasNext()) {
 *    TreeNode node = iterator.next();
 *    do something for node
 * } 
 */
public class Solution {
    //@param root: The root of binary tree.
    public Solution(TreeNode root) {
        // write your code here
        s = new Stack<TreeNode> ();
        TreeNode current;
        current = root;
        while (current != null) {
            s.push(current);
            current = current.left;
        }
    }

    //@return: True if there has next node, or false
    public boolean hasNext() {
        // write your code here
        return !(this.s.empty());
    }
    
    //@return: return next node
    public TreeNode next() {
        // write your code here
//	System.out.println(s);
        TreeNode res = s.pop();
        if (res.right != null) {
            TreeNode current = res.right;
            while (current != null) {
                s.push(current);
                current = current.left;
            }
        }
        return res;
    }
    
    public Stack<TreeNode> s;
    public static void main(String[] args) {
	TreeNode root = new TreeNode(-1);
	Solution iterator = new Solution(root);
	while (iterator.hasNext()) {
	    System.out.println(iterator.next().val);
	}
    }
}


