/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode *sortedListToBST(ListNode *head) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        TreeNode *root;
        int i,k,n;
        ListNode *l,*head2,*p;
        if(head==NULL) {root=NULL;return root;}
        else {
            l=head;
            i=0;
            while(l!=NULL) {++i;l=l->next;}
            n=i;
            k=n/2;
            l=head;
            if(k==0) {
                root=new TreeNode(l->val);return root;
            }
            else {
                for(i=0;i<k;i++) {p=l;l=l->next;}
                head2=l->next;
                p->next=NULL;
                root=new TreeNode(l->val);
                root->left=sortedListToBST(head);
                root->right=sortedListToBST(head2);
                return root;
            }
        }
    }
};
