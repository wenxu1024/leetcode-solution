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
    ListNode *insertionSortList(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head==NULL) return head;
        else   {
            ListNode* newhead,*prev,*l;
            newhead=insertionSortList(head->next);
            l=newhead;
            while(l!=NULL&&head->val>l->val) {prev=l; l=l->next;}
            if(l==newhead) {head->next=newhead;return head;}
            else if(l==NULL) {prev->next=head;head->next=NULL;return newhead;}
            else {prev->next=head;head->next=l;return newhead;}
        }
    }
};
