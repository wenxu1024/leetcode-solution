class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        sort(num);
        int a,b,c,n,i,j;
        vector<vector<int> > vv;
        vector<int> v;
        set<vector<int> > s;
        n=num.size();
        if(n<3) return vv;
        if(num[0]>0) return vv;
        if(num[n-1]<0) return vv;
        
        for(i=0;i<n-2;i++) {
            for(j=i+1;j<n-1;j++) {
                a=num[i];
                b=num[j];
                c=0-a-b;
                if(find(num,j+1,n-1,c)) {
                    v.clear();
                    v.push_back(a);
                    v.push_back(b);
                    v.push_back(c);
                    if(s.find(v)==s.end()) {
                    vv.push_back(v);
                    s.insert(v);
                    }
                }
            }
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
    
    bool find(vector<int> &num, int i, int j, int c) {
        if(i>j) return false;
        int m;
        m=(i+j)/2;
        if(c==num[m]) return true;
        else if(c<num[m]) {
            return find(num,i,m-1,c);
        }
        else {
            return find(num,m+1,j,c);
        }
    }
};
