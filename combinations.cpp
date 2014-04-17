class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        vector<int> v;
        vector<vector<int> > vv,vv1,vv2;
        int i,l,m;
        if(n<k) return vv;
        if(k==0) {vv.push_back(v);return vv;}
        vv1=combine(n-1,k-1);
        vv2=combine(n-1,k);
        l=vv1.size();
        m=vv2.size();
        for(i=0;i<l;i++) {
            vv1[i].push_back(n);
            vv.push_back(vv1[i]);
        }
        for(i=0;i<m;i++) {
            vv.push_back(vv2[i]);
        }
        return vv;
    }
};
