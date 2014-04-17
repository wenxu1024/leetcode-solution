class Solution {
public:
    int maxSubArray(int A[], int n) {
        if(n==1) return A[0];
        int B[1000000];
        int i;
        int bt=0;
        for(i=0;i<n;i++) {
            bt+=A[i];
            B[i]=bt;
        }
        return maxdifference(B,0,n-1);
    }
    
    int maxdifference(int B[],int i, int j) {
        if(i==j) return B[i];
        else {
            int b1,b2,b3,bf;
            int m;
            m=(i+j)/2;
            b1=maxdifference(B,i,m);
            b2=maxdifference(B,m+1,j);
            int k,min,max;
            min=10000000;
            max=-10000000;
            for(k=m;k>=i;k--) min=(B[k]<min) ? B[k]: min;
            for(k=m+1;k<=j;k++) max=(B[k]>max) ? B[k]:max;
            b3=max-min;
            bf=(b1>b2)? b1: b2;
            bf=(b3>bf)? b3: bf;
            return bf;
        }
    }
};
