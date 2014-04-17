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
    void flatten(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) return;
        if(root->left==NULL&&root->right==NULL) return;
        else if(root->left!=NULL&&root->right==NULL) {flatten(root->left);root->right=root->left;root->left=NULL;return;}
        else if(root->left==NULL&&root->right!=NULL) {flatten(root->right);return;}
        else {
            flatten(root->left);
            flatten(root->right);
            TreeNode *t;
            t=root->left;
            while(t->right!=NULL) {t=t->right;}
            t->right=root->right;
            root->right=root->left;
            root->left=NULL;
            return;
        }
    }
};
