class Solution {
public:
    vector<int> grayCode(int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        vector<int> v,v2;
        if(n==0) {v.push_back(0);return v;}
        if(n==1) {
            v.push_back(0);
            v.push_back(1);
            return v;
        }
        v2=grayCode(n-1);
        int m,i,d;
        d=1<<(n-1);
        m=v2.size();
        for(i=0;i<m;i++) {
            v.push_back(v2[i]);
        }
        for(i=m-1;i>=0;i--) {
            v.push_back(v2[i]+d);
        }
        return v;
    }
};
