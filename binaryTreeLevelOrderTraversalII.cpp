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
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > vv,vv1,vv2,vv3;
        vector<int> v;
        if(root==NULL) return vv;
        if(root->left==NULL&&root->right==NULL) {v.push_back(root->val);vv.push_back(v);return vv;}
        else if(root->left!=NULL&&root->right==NULL) {
            vv=levelOrderBottom(root->left);
            v.push_back(root->val);
            vv.push_back(v);
            return vv;
        }
        else if(root->left==NULL&&root->right!=NULL) {
            vv=levelOrderBottom(root->right);
            v.push_back(root->val);
            vv.push_back(v);
            return vv;
        }
        else {
            vv1=levelOrderBottom(root->left);
            vv2=levelOrderBottom(root->right);
            int m,n,i,j,l;
            m=vv1.size();
            n=vv2.size();
            for(i=0;i<m&&i<n;i++) {
                v.clear();
                l=vv1[m-1-i].size();
                for(j=0;j<l;j++) v.push_back(vv1[m-1-i][j]);
                l=vv2[n-1-i].size();
                for(j=0;j<l;j++) v.push_back(vv2[n-1-i][j]);
                vv3.push_back(v);
            }
            for(;i<m;i++) {
                vv3.push_back(vv1[m-1-i]);
            }
            for(;i<n;i++) {
                vv3.push_back(vv2[n-1-i]);
            }
            n=vv3.size();
            for(i=0;i<n;i++) vv.push_back(vv3[n-1-i]);
            v.clear();
            v.push_back(root->val);
            vv.push_back(v);
            return vv;
        }
        
    }
};
