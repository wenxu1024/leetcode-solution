/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n;
        TreeNode *head;
        n=postorder.size();
        head=build(inorder,postorder,0,0,n);
        return head;
    }
    
    
    TreeNode* build(vector<int> &inorder, vector<int> &postorder, int i, int j, int l) {//i is starting position of inorder, j is the starting position of postorer, l is the length
        int k;
        TreeNode *head;
        if(l<=0) return NULL;
        else {
            for(k=0;k<l&&inorder[i+k]!=postorder[j+l-1];k++) {}
            head=new TreeNode(postorder[j+l-1]);
            head->left=build(inorder,postorder,i,j,k);
            head->right=build(inorder,postorder,i+k+1,j+k,l-k-1);
            return head;
        }
    }
};
