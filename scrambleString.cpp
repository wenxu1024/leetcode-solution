class Solution {
public:
    bool isScramble(string s1, string s2) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        bool c[100][100][100];
        int i,j,l,n,m;
        n=s2.size();
        if(n==0) return true;
        for(i=0;i<n;i++) {
            for(j=0;j<n;j++) {
                if(s1[i]==s2[j]) c[i][j][1]=true;
                else c[i][j][1]=false;
            }
        }
        for(l=2;l<=n;l++) {
            for(i=n-l;i>=0;i--) {
                for(j=n-l;j>=0;j--) {
                    c[i][j][l]=false;
                    for(m=1;m<=l-1;m++) {
                        c[i][j][l]=c[i][j][l]||(c[i][j][m]&&c[i+m][j+m][l-m])||(c[i][j+l-m][m]&&c[i+m][j][l-m]);
                    }
                }
            }
        }
        return c[0][0][n];
    }
};
