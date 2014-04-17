class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int i,j,n,k;
        string substr;
        bool wb[1000][1000];
        n=s.size();
        for(i=0;i<n;i++) {
            substr=s.substr(i,1);
            if(dict.find(substr)!=dict.end()) wb[i][i]=true;
            else wb[i][i]=false;
        }
        for(i=2;i<=n;i++) {//len
            for(j=0;j<=n-i;j++) {//starting position
            substr=s.substr(j,i);
            if(dict.find(substr)!=dict.end()) wb[j][j+i-1]=true;
            else wb[j][j+i-1]=false;
                for(k=j;k<j+i-1;k++) {
                    wb[j][j+i-1]=wb[j][j+i-1]||(wb[j][k]&&wb[k+1][j+i-1]);
                }
            }
        }
        return wb[0][n-1];
    }
};
