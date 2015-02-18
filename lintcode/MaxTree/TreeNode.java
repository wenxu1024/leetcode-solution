//TreeNode.java
public class TreeNode {
      public int val;
      public TreeNode left, right;
      public TreeNode(int val) {
          this.val = val;
          this.left = this.right = null;
      }

      public String toString() {
	  String res;
	  res = ""+ val;
	  return res;
      }
  }

