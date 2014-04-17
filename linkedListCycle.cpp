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
    bool hasCycle(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        set<ListNode*> s;
        if(head==NULL) return false;
        s.insert(head);
        ListNode* l;
        l=head->next;
        while(l!=NULL&&s.find(l)==s.end()) {
            s.insert(l);
            l=l->next;
        }
        if(l==NULL) return false;
        else return true;
    }
};
