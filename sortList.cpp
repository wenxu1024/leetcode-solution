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
    ListNode *sortList(ListNode *head) {
        ListNode *l,*head2,*head1,*nwhead;
        l=head;
        int i,n;
        n=0;
        while(l!=NULL) {n++;l=l->next;}
        l=head;
        if(n<=1) return head;
        else {
            for(i=0;i<n/2-1;i++) {
            l=l->next;
        }
        head2=l->next;
        l->next=NULL;
        head1=sortList(head);
        head2=sortList(head2);
        nwhead=mergeTwoLists(head1,head2);
        return nwhead;
        }
    }
    
    
        ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *head;
        if(l1==NULL&&l2!=NULL) return l2;
        else if(l1==NULL&&l2==NULL) return NULL;
        else if(l1!=NULL&&l2==NULL) return l1;
        else {
            if(l1->val<l2->val) {
                head=l1;
                head->next=mergeTwoLists(l1->next,l2);
            }
            else {
                head=l2;
                head->next=mergeTwoLists(l1,l2->next);
            }
            return head;
        }
    }
};
