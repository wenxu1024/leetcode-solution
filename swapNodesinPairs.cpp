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
    ListNode *swapPairs(ListNode *head) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ListNode *l,*nh;
        if(head==NULL) return head;
        if(head->next==NULL) return head;
        l=swapPairs(head->next->next);
        nh=head->next;
        nh->next=head;
        head->next=l;
        return nh;
    }
};
