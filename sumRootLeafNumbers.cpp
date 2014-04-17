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
    int sumNumbers(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<TreeNode*> vt;
        TreeNode* t;
        int sum;
        sum=0;
        t=root;
        vt.push_back(t);
        while(t!=NULL&&vt.size()!=0) {
            t=vt.back();
            vt.pop_back();
            if(t->left!=NULL) {
                vt.push_back(t->left);
                t->left->val+=t->val*10;
            }
            if(t->right!=NULL) {
                vt.push_back(t->right);
                t->right->val+=t->val*10;
            }
            
        }
        
        t=root;
        vt.push_back(t);
        while(t!=NULL&&vt.size()!=0) {
            t=vt.back();
            vt.pop_back();
            if(t->left==NULL&&t->right==NULL) sum=sum+t->val;
            if(t->left!=NULL) {
                vt.push_back(t->left);
            }
            if(t->right!=NULL) {
                vt.push_back(t->right);
            }
        }
        return sum;
    }
};
