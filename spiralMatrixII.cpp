class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> v;
        vector<vector<int> > vv,vv1;
        int j,i;
        if(n==0) return vv;
        if(n==1) {v.push_back(1);vv.push_back(v);return vv;}
        if(n==2) {
            v.push_back(1);v.push_back(2);
            vv.push_back(v);
            v.clear();
            v.push_back(4);v.push_back(3);
            vv.push_back(v);
            return vv;
        }
        vv1=generateMatrix(n-2);
        for(j=0;j<n;j++) v.push_back(j+1);
        vv.push_back(v);
        v.clear();
        int m;
        m=vv1.size();
        for(i=0;i<m;i++) {
            v.push_back(4*n-4-i);
            for(j=0;j<m;j++) v.push_back(vv1[i][j]+4*n-4);
            v.push_back(n+1+i);
            vv.push_back(v);
            v.clear();
        }
        for(i=0;i<n;i++) {
            v.push_back(3*n-2-i);
        }
        vv.push_back(v);
        return vv;
    }
};
