class Solution {
public:
    int uniquePaths(int m, int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int C[200][200];
        int i,j,k;
        for(i=1;i<=m;i++) C[i][1]=1;
        for(j=1;j<=n;j++) C[1][j]=1;
        for(i=2;i<=m;i++) {
            for(j=2;j<=n;j++) {
                C[i][j]=0;
                for(k=1;k<=j-1;k++) C[i][j]+=C[i-1][k];
                for(k=1;k<=i-1;k++) C[i][j]+=C[k][j-1];
            }
        }
        return C[m][n];
    }
};
