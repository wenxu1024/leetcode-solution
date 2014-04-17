class Solution {
public:
    int maxProfit(vector<int> &prices) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int n,i,j,max,max1,p1,p2;
        n=prices.size();
        if(n==0) return 0;
        max=0;
        p1=prices[0];
        for(i=0;i<n;i++) {
            if(prices[i]>=p1) {
                max1=prices[i]-p1;
                max=(max1>max)? max1:max;
            }
            else {
                p1=prices[i];
            }
        }
        return max;
    }
};
