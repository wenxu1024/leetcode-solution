class Solution {
public:
    void sortColors(int A[], int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int B[3][10000];
        int j,k,l,i;
        j=0;
        k=0;
        l=0;
        for(i=0;i<n;i++) {
            if(A[i]==0) {B[0][j]=0;j++;}
            else if(A[i]==1) {B[1][k]=1;k++;}
            else {B[2][l]=2;l++;}
        }
        for(i=0;i<j;i++) A[i]=B[0][i];
        for(i=j;i<j+k;i++) A[i]=B[1][i-j];
        for(i=j+k;i<j+k+l;i++) A[i]=B[2][i-j-k];
        return;
    }
};
