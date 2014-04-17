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
    bool hasPathSum(TreeNode *root, int sum) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) {return false;}
        if(root->left==NULL&&root->right==NULL) {if(root->val==sum) return true; else return false;}
        int sum1;
        sum1=sum-root->val;
        return (hasPathSum(root->left,sum1)||hasPathSum(root->right,sum1));
    }
};
