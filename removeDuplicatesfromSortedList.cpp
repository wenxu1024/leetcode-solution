/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        ListNode *l;
        l=head;
        if(head==NULL) return head;
        if(head->next==NULL) return head;
        while(l->next!=NULL) {
            if(l->val==l->next->val) {
                l->next=l->next->next;
            }
            else l=l->next;
        }
        return head;
    }
};
