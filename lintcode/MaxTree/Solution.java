import java.util.*;

//Max Tree, Building Cartesian Tree in O(n) time

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
public class Solution {
    /**
     * @param A: Given an integer array with no duplicates.
     * @return: The root of max tree.
     */
    public TreeNode maxTree(int[] A) {
        // write your code here
        int i, l = A.length;
        if (l == 0) return null;
        TreeNode ctemp, temp, current,prev;
        current = new TreeNode(A[0]);
        Map<TreeNode, TreeNode> parent = new HashMap<TreeNode, TreeNode> ();
        parent.put(current, null);
        prev = current;
        for(i = 1; i < l; i ++) {
            current = new TreeNode(A[i]);
            if (current.val < prev.val) {
                prev.right = current;
                parent.put(current, prev);
                prev = current;
            }
            else {
                temp = prev;
                ctemp = null;
                while (temp != null) {
                    if (temp.val > current.val) break;
                    ctemp = temp;
                    temp = parent.get(temp);
                    
                }
                if (temp == null) {
                    current.left = ctemp;
                    parent.put(ctemp, current);
                    parent.put(current, null);
                }
                else {
                    current.left = temp.right;
                    parent.put(temp.right, current);
                    temp.right = current;
                    parent.put(current, temp);
                }
                prev = current;
            }
        }
        TreeNode root;
        while (parent.get(prev) != null) {
            prev = parent.get(prev);
        }
        root = prev;
        return root;
    }
}


