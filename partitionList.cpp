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
    ListNode *partition(ListNode *head, int x) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(head==NULL) return head;
        if(head->val<x) {
            ListNode* h;
            h=partition(head->next,x);
            head->next=h;
            return head;
        }   
        else {
            ListNode *h,*l,*p;
            h=partition(head->next,x);
            l=h;
            if(h==NULL) return head;
            else {
            if(h->val>=x) {head->next=h; return head;}
            else {
            while(h!=NULL&&h->val<x) {p=h; h=h->next;}  
            p->next=head;
            head->next=h;
            return l;
            }
            }
            }
    }
};
