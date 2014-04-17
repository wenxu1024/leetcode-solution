class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        int i,j,n,l;
        string s;
        n=strs.size();
        if(n==0) return s;
        else {
            l=strs[0].size();
            for(j=0;j<l;j++) {
                for(i=0;i<n;i++) {
                    if(j<strs[i].size()) {
                        if(strs[i][j]!=strs[0][j]) break;
                    }
                    else break;
                }
                if(i==n) {s+=strs[0][j];}
                else break;
            }
            return s;
        }
    }
};
