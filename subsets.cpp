class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n,a,m,i;
        vector<vector<int> > vv,vv1;
        vector<int> v;
        n=S.size();
        if(n==0) {vv.push_back(v);return vv;}
        sort(S);
        a=S[n-1];
        S.pop_back();
        vv1=subsets(S);
        m=vv1.size();
        for(i=0;i<m;i++) {
            vv.push_back(vv1[i]);
            vv1[i].push_back(a);
            vv.push_back(vv1[i]);
        }
        return vv;
    }
    
    void sort(vector<int> &S) {
        int i,j,n,temp;
        n=S.size();
        for(i=0;i<n-1;i++) {
            for(j=i+1;j>=1;j--) {
                if(S[j]<S[j-1]) {
                    temp=S[j];
                    S[j]=S[j-1];
                    S[j-1]=temp;
                }
            }
        }
        return;
    }
};
