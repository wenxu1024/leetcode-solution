class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int C[10000];
        int n,i,l,j;
        set<int> st;
        n=s.size();
        C[1]=1;
        for(i=1;i<=n;i++) {
            l=0;
            st.clear();
            for(j=i-1;j>=0;j--) {
                if(st.find(s[j])==st.end()) {l++;st.insert(s[j]);}
                else break;
            }
            C[i]=(C[i-1]>l)? C[i-1]:l;
        }
        return C[n];
    }
};
