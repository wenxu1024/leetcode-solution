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
    vector<TreeNode *> generateTrees(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        return gen(1,n);
    }
    
    
    vector<TreeNode*> gen(int start, int end) {
        vector<TreeNode*> f1,f2,f3;
        TreeNode* root;
        int i,n,k,m,j;
        if(start>end) {f1.push_back(NULL); return f1;}
        else if(start==end) {root=new TreeNode(start); f1.push_back(root); return f1;}
        else {
            f1=gen(start+1,end);
            n=f1.size();
            for(i=0;i<n;i++) {
                root=new TreeNode(start);
                root->right=f1[i];
                f2.push_back(root);
            }
            for(i=start;i<=end-2;i++) {
                f1=gen(start,i);
                f3=gen(i+2,end);
                m=f1.size();
                n=f3.size();
                for(j=0;j<m;j++) {
                    for(k=0;k<n;k++) {
                        root=new TreeNode(i+1);
                        root->left=f1[j];
                        root->right=f3[k];
                        f2.push_back(root);
                    }
                }
            }
            f1=gen(start,end-1);
            n=f1.size();
            for(i=0;i<n;i++) {
                root=new TreeNode(end);
                root->left=f1[i];
                f2.push_back(root);
            }
            return f2;
        }
    }
};
