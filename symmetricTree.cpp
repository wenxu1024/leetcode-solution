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
    bool isSymmetric(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) return true;
        else if(root->left==NULL&&root->right==NULL) return true;
        else if(root->left==NULL&&root->right!=NULL) return false;
        else if(root->left!=NULL&&root->right==NULL) return false;
        else {
            if(!isSymmTree(root->left,root->right)) return false;
            else return true;
        }
    }
    
    bool isSymmTree(TreeNode *p, TreeNode *q) {
        if(p==NULL&&q==NULL) return true;
        else if(p==NULL&&q!=NULL) return false;
        else if(p!=NULL&&q==NULL) return false;
        else {
            if(p->val!=q->val) return false;
            else {
                if(!isSymmTree(p->left,q->right)||!isSymmTree(p->right,q->left)) return false;
                else return true;
            }
        }
    }
};
