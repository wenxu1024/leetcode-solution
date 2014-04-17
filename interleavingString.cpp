class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        bool B[1000][1000];
        int i,j,m,n,l;
        m=s1.size();
        n=s2.size();
        l=s3.size();
        if((m+n)!=l) return false;
        for(i=0;i<=m;i++) {
            if(s1.substr(0,i)==s3.substr(0,i)) B[i][0]=true;
            else B[i][0]=false;
        }
        for(j=0;j<=n;j++) {
            if(s2.substr(0,j)==s3.substr(0,j)) B[0][j]=true;
            else B[0][j]=false;
        }
        for(i=1;i<=m;i++) {
            for(j=1;j<=n;j++) {
                if(s3[i+j-1]==s1[i-1]&&s3[i+j-1]==s2[j-1])
                B[i][j]=(B[i-1][j]||B[i][j-1]);
                else if(s3[i+j-1]==s1[i-1]&&s3[i+j-1]!=s2[j-1])
                B[i][j]=B[i-1][j];
                else if(s3[i+j-1]!=s1[i-1]&&s3[i+j-1]==s2[j-1])
                B[i][j]=B[i][j-1];
                else 
                B[i][j]=false;
            }
        }
        return B[m][n];
    }
};
