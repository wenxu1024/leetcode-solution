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
    vector<int> postorderTraversal(TreeNode *root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case
        vector<int> v,v1,v2;
        if(root==NULL) return v;
        else {
            v1=postorderTraversal(root->left);
            v2=postorderTraversal(root->right);
            v.insert(v.end(),v1.begin(),v1.end());
            v.insert(v.end(),v2.begin(),v2.end());
            v.insert(v.end(),root->val);
            return v;
        }
        
    }
};
