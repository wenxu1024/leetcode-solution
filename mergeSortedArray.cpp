class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int C[m+1],D[n+1];
        int i,j,k;
        for(i=0;i<m;i++) C[i]=A[i];
        C[m]=INFINITY;
        for(i=0;i<n;i++) D[i]=B[i];
        D[n]=INFINITY;
        i=0;
        j=0;
        for(k=0;k<m+n;k++) {
            if(C[i]<D[j]) {
                A[k]=C[i];
                i++;
                }
            else {
                A[k]=D[j];
                j++;
            }
        }
        return;
    }
};

