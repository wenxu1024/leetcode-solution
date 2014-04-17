class Solution {
public:
    int singleNumber(int A[], int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        set<int> s;
        set<int> s2;
        int i;
        s.insert(A[0]);
        set<int>::iterator it,it1;
        for(i=1;i<n;i++) {
            it=s.find(A[i]);
            if(it==s.end()) s.insert(A[i]);
            else {s2.insert(*it); s.erase(it);}
        }
        for(it1=s2.begin();it1!=s2.end();++it1) {
            s.erase(*it1);
        }
        it=s.begin();
        return *it;
    }
};
