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
    int minDepth(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) return 0;
        if(root->left==NULL&&root->right==NULL) return 1;
        else if(root->left==NULL&&root->right!=NULL) return 1+minDepth(root->right);
        else if(root->left!=NULL&&root->right==NULL) return 1+minDepth(root->left);
        else {
            int hl,hr,h;
            hl=minDepth(root->left);
            hr=minDepth(root->right);
            h=(hl<hr)? hl: hr;
            h++;
            return h;
        }
    }
};
