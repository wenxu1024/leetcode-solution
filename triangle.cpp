class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> v1,v2;
        int m,n,i,j,k,l,t,min;
        m=triangle.size();
        if(m==0) return 0;
        if(m==1) return triangle[0][0];
        v2=triangle[0];
        for(i=1;i<m;i++) {
            n=triangle[i].size();
            for(j=0;j<n;j++) {
                if(j==0) {
                    v1.push_back(triangle[i][j]+v2[j]);
                }
                else if(j==n-1) {
                    v1.push_back(triangle[i][j]+v2[j-1]);
                }
                else {
                    k=triangle[i][j]+v2[j];
                    l=triangle[i][j]+v2[j-1];
                    t=(k<l)? k:l;
                    v1.push_back(t);
                }
                }
            v2=v1;
            v1.clear();
        }
        n=v2.size();
        min=v2[0];
        for(i=0;i<n;i++) {min=(v2[i]<min)? v2[i]: min;}
        return min;
    }
};
