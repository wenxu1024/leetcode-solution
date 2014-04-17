class Solution {
public:
    void nextPermutation(vector<int> &num) {
        int k,l,n;
        n=num.size();
        if(n<=1) return;
        for(k=n-2;k>=0;k--) {
            if(num[k+1]>num[k]) {
                for(l=n-1;l>k;l--) {
                    if(num[l]>num[k]) break;
                }
                swap(num,k,l);
                reverse(num,k+1,n-1);
                return;
            }
        }
        reverse(num,0,n-1);
        return;
    }
    
    void swap(vector<int> &num, int k, int l) {
        int temp;
        temp=num[k];
        num[k]=num[l];
        num[l]=temp;
        return;
    }
    
    void reverse(vector<int>& num, int k, int l) {
        int i,m;
        m=(k+l)/2;
        for(i=k;i<=m;i++) swap(num,i,l-i+k);
        return;
    }
};
