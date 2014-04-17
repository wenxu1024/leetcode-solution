/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(root==NULL) return;
        if(root->left==NULL&&root->right==NULL) {root->next=NULL;return;}
        else if(root->left!=NULL&&root->right==NULL) {
            root->next=NULL;
            connect(root->left);
            return;
        }
        else if(root->left==NULL&&root->right!=NULL) {
            root->next=NULL;
            connect(root->right);
            return;
        }
        else {
            root->next=NULL;
            connect(root->left);
            connect(root->right);
            TreeLinkNode *t1,*t2;
            t1=root->left;
            t2=root->right;
            while(t1!=NULL&&t2!=NULL) {t1->next=t2;t1=t1->right;t2=t2->left;}
            return;
        }
    }
};
