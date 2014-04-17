class Solution {
public:
    int climbStairs(int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int f[10000],i;
        f[1]=1;
        f[2]=2;
        for(i=3;i<=n;i++) {
            f[i]=f[i-1]+f[i-2];
        }
        return f[n];
    }
};
