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
    bool isValidBST(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) return true;
        if(root->left==NULL&&root->right==NULL) return true;
        if(root->left!=NULL&&root->right==NULL) {
            if(root->val<=maxBST(root->left)) return false;
            else {
                if(!isValidBST(root->left)) return false;
                else return true;
            }
        }
        if(root->left==NULL&&root->right!=NULL) {
            if(root->val>=minBST(root->right)) return false;
            else {
                if(!isValidBST(root->right)) return false;
                else return true;
            }
        }
        if(root->left!=NULL&&root->right!=NULL) {
            if(root->val<=maxBST(root->left)||root->val>=minBST(root->right)) return false;
            else {
                if(!isValidBST(root->left)||!isValidBST(root->right)) return false;
                else return true;
            }
        }
    }
    
    int maxBST(TreeNode *root) {
        TreeNode *t;
        t=root;
        while(t->right!=NULL) {t=t->right;}
        return t->val;
    }
    
    int minBST(TreeNode *root) {
        TreeNode *t;
        t=root;
        while(t->left!=NULL) {t=t->left;}
        return t->val;
    }
};
