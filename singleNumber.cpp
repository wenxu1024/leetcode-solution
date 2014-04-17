class Solution {
public:
    int singleNumber(int A[], int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        set<int> s;
        set<int>::iterator it;
        int i;
        s.insert(A[0]);
        for(i=1;i<n;i++) {
             it=s.find(A[i]);
             if(it!=s.end()) s.erase(it);
             else s.insert(A[i]);
        }
        it=s.begin();
        return *it;
    }
};
