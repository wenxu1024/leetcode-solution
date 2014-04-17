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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        ListNode *temp,*current,*previous,*pm,*pn,*temp2,*list;
        int i;  
        temp=head;
        temp2=temp;
        if (m==1) pm=head;
        else { for(i=0;i<m-1;i++) {head=head->next;pm=head;}}
        if (n==1) pn=temp;
        else { for(i=0;i<n-1;i++) {temp=temp->next;pn=temp;}}
        previous=pn->next;
        current=pm;
        for(i=0;i<=n-m;i++) {
            temp=pm->next;
            pm->next=previous;
            previous=pm;
            pm=temp;
        }       
        if (m==1) {return previous;}
        else {  
        list=temp2;
        while(temp2->next!=current) temp2=temp2->next;
        temp2->next=previous;
        return list;
        }
    }
};
