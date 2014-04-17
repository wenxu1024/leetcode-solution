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
    void recoverTree(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        TreeNode *t1,*t2;
        int temp;
        if(root==NULL) return;
        if(root->left==NULL&&root->right==NULL) return;
        else if(root->left==NULL&&root->right!=NULL) {
            t1=min(root->right);
            if(root->val>t1->val) {
            temp=root->val;
            root->val=t1->val;
            t1->val=temp;
            }
            else {
                recoverTree(root->right);
            }
            return;
        }
        else if(root->left!=NULL&&root->right==NULL) {
            t1=max(root->left);
            if(root->val<t1->val) {
                temp=root->val;
                root->val=t1->val;
                t1->val=temp;
            }
            else {
                recoverTree(root->left);
            }
            return;
        }
        else {
            t1=max(root->left);
            t2=min(root->right);
            if(root->val<t1->val&&root->val>t2->val) {
                temp=t1->val;
                t1->val=t2->val;
                t2->val=temp;
            }
            else if(root->val<t1->val&&root->val<=t2->val) {
                temp=root->val;
                root->val=t1->val;
                t1->val=temp;
            }
            else if(root->val>=t1->val&&root->val>t2->val) {
                temp=root->val;
                root->val=t2->val;
                t2->val=temp;
            }
            else {
                recoverTree(root->left);
                recoverTree(root->right);
            }
            return;
        }
        }
    
    
    TreeNode* max(TreeNode *root) {
        TreeNode *t,*t1,*t2;
        if(root->left==NULL&&root->right==NULL) return root;
        else if(root->left==NULL&&root->right!=NULL) {
            t=max(root->right);
            if(t->val>root->val) return t;
            else return root;
        }
        else if(root->left!=NULL&&root->right==NULL) {
            t=max(root->left);
            if(t->val>root->val) return t;
            else return root;
        }
        else {
            t1=max(root->left);
            t2=max(root->right);
            t=(t1->val>t2->val) ? t1: t2;
            t=(root->val>t->val) ? root: t;
            return t;
        }
    }
    
    TreeNode* min(TreeNode *root) {
        TreeNode *t,*t1,*t2;
        if(root->left==NULL&&root->right==NULL) return root;
        else if(root->left==NULL&&root->right!=NULL) {
            t=min(root->right);
            if(t->val<root->val) return t;
            else return root;
        }
        else if(root->left!=NULL&&root->right==NULL) {
            t=min(root->left);
            if(t->val<root->val) return t;
            else return root;
        }
        else {
            t1=min(root->left);
            t2=min(root->right);
            t=(t1->val<t2->val) ? t1: t2;
            t=(root->val<t->val) ? root: t;
            return t;
        }
    }
};
