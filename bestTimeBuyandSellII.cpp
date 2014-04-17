class Solution {
public:
    int maxProfit(vector<int> &prices) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int n,i;
        int p1,p2;
        int max,max1,max2;
        max=0;
        max2=0;
        n=prices.size();
        if(n==0) return 0;
        p1=prices[0];
        p2=prices[0];
        for(i=0;i<n;i++) {
            if(prices[i]>=p2) {
                p2=prices[i];
            }
            else {
                max1=p2-p1;
                max2=(max1>max2)? max1: max2;
                max+=max2;
                p1=prices[i];
                p2=p1;
                max2=0;
            }
        }
        max1=p2-p1;
        max+=max1;
        return max;
    }
};
