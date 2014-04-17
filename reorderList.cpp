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
    void reorderList(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode* larray[100000];
        int i,n;
        ListNode *l;
        i=0;
        l=head;
        while(l!=NULL) {
            larray[i]=l;
            l=l->next;
            i++;
        }
        n=i;
        if(n<=2) return;
        else {
            for(i=0;i<n/2;i++) {
                larray[i]->next=larray[n-i-1];
                larray[n-i-1]->next=larray[i+1];
            }
            larray[i]->next=NULL;
        }
        return;
    }
};
