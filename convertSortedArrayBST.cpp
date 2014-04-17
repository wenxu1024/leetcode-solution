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
    TreeNode *sortedArrayToBST(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        TreeNode *root;
        vector<int> num1, num2;
        int n,i,k;
        n=num.size();
        if(n==0) {root=NULL;return root;}
        else {
            k=n/2;
            for(i=0;i<k;i++) {num1.push_back(num[i]);}
            for(i=k+1;i<n;i++) {num2.push_back(num[i]);}
            root= new TreeNode(num[k]);
            root->left=sortedArrayToBST(num1);
            root->right=sortedArrayToBST(num2);
            return root;
        }
    }
    
};
