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
    int maxDepth(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) return 0;
        int hl,hr,h;
        hl=maxDepth(root->left);
        hr=maxDepth(root->right);
        h=(hl>hr) ? hl: hr;
        h++;
        return h;
    }
};
