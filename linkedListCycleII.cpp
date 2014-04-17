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
    ListNode *detectCycle(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        set<ListNode*> s;
        ListNode* l;
        if(head==NULL) return head;
        s.insert(head);
        l=head->next;
        while(l!=NULL&&s.find(l)==s.end()) {
            s.insert(l);
            l=l->next;
        }
        return  l;
    }
};
