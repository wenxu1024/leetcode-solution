class Solution {
public:
    int numTrees(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> f;
        int m;
        int i,j;
        f.push_back(0);
        f.push_back(1);
        for(i=2;i<=n;i++) {
            m=2*f[i-1];
            for(j=0;j<=i-1;j++) {
                m+=f[j]*f[i-1-j];
            }
            f.push_back(m);
        }
        return f[n];
    }
};
