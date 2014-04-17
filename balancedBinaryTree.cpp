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
    bool isBalanced(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) return true;
        int hl,hr;
        hl=height(root->left);
        hr=height(root->right);
        if(hl-hr<-1||hl-hr>1) return false;
        else {
            if(!isBalanced(root->left)||!isBalanced(root->right)) return false;
            else return true;
        }
    }
    
    int height(TreeNode *root) {
        if(root==NULL) return 0;
        int hl,hr,h;
        hl=height(root->left);
        hr=height(root->right);
        h=(hl>hr) ? hl:hr;
        h++;
        return h;
    }
};
