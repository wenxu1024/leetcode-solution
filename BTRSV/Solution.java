/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        ArrayList<ArrayList<Integer> > layers = new ArrayList<ArrayList<Integer> > ();
        Queue<Pair<TreeNode, Integer> > q = new LinkedList<Pair<TreeNode, Integer> >();
        List<Integer> res = new ArrayList<Integer> ();
        if (root == null) return res;
        Pair<TreeNode, Integer> rootpair = new Pair(root, 0);
        q.add(rootpair);
        while (!q.isEmpty()) {
            Pair<TreeNode, Integer> current = q.poll();
            if (layers.size() < current.layer + 1) {
                ArrayList<Integer> singlelayer = new ArrayList<Integer>();
                singlelayer.add(current.node.val);
                layers.add(singlelayer);
            }
            else {
                layers.get(current.layer).add(current.node.val);
            }
            if (current.node.left != null) {
                Pair<TreeNode, Integer> leftpair = new Pair(current.node.left, current.layer + 1);
                q.add(leftpair);
            }
            if (current.node.right != null) {
                Pair<TreeNode, Integer> rightpair = new Pair(current.node.right, current.layer + 1);
                q.add(rightpair);
            }
        }
        int length = layers.size();
        for(int i = 0; i < length; i ++) {
            ArrayList<Integer> ithLayer = layers.get(i);
            int sizeOfLayer = ithLayer.size();
            int lastNumber = ithLayer.get(sizeOfLayer - 1);
            res.add(lastNumber);
        }
        return res;
}
}

class Pair<TreeNode, Integer> {
    TreeNode node;
    int layer;
    
    public Pair(TreeNode node, int layer) {
        this.node = node;
        this.layer = layer;
    }
}
