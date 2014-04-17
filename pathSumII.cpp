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
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<vector<int> > vv,vv1,vv2;
        vector<int> v;
        int sum1;
        if(root==NULL) return vv;
        if(root->left==NULL&&root->right==NULL) {
            v.clear();
            if(root->val==sum) {v.push_back(root->val);vv.push_back(v); return vv;}
            else return vv;
        }
        
        sum1=sum-root->val;
        vv1=pathSum(root->left,sum1);
        vv2=pathSum(root->right,sum1);
        int m,n,i;
        m=vv1.size();
        n=vv2.size();
        for(i=0;i<m;i++) {
            v=vv1[i];
            v.insert(v.begin(),root->val);
            vv.push_back(v);
        }
        for(i=0;i<n;i++) {
            v=vv2[i];
            v.insert(v.begin(),root->val);
            vv.push_back(v);
        }
        return vv;
    }
};
