class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        vector<int> v,v1;
        vector<vector<int> > vv;
        int n,d,i,k,temp;
        n=numbers.size();
        for(i=0;i<n;i++) {v.push_back(i);v.push_back(numbers[i]);vv.push_back(v);v.clear();}
        mergesort(vv);
        for(i=0;i<n-1;i++) {
            d=target-vv[i][1];
            k=find(vv,i+1,n-1,d);
            if(k!=-1) {
                v.push_back(vv[i][0]+1);
                v.push_back(vv[k][0]+1);
                if(v[0]>v[1]) {
                    temp=v[0];
                    v[0]=v[1];
                    v[1]=temp;
                    }
                return v;    
                }
        }
        return v;
    }


    void mergesort(vector<vector<int> > &vv) {
        int l,i;
        vector<vector<int> >vv1,vv2;
        l=vv.size();
        if(l==1) return;
        for(i=0;i<l/2;i++) vv1.push_back(vv[i]);
        for(i=l/2;i<l;i++) vv2.push_back(vv[i]);
        mergesort(vv1);
        mergesort(vv2);
        vv=merge(vv1,vv2);
        return;
    }

    
    
        vector<vector<int> > merge(vector<vector<int> > vv1, vector<vector<int> > vv2) {
        int i,j,k,m,n;
        vector<int> v;
        vector<vector<int> > vv;
        m=vv1.size();
        n=vv2.size();
        v.push_back(0);
        v.push_back(INFINITY);
        vv1.push_back(v);
        vv2.push_back(v);
        i=0;
        j=0;
        for(k=0;k<m+n;k++) {
            if(vv1[i][1]<vv2[j][1]) {
                vv.push_back(vv1[i]);
                i++;
                }
            else {
                vv.push_back(vv2[j]);
                j++;
            }
        }
        return vv;
   }


    int find(vector<vector<int> > &vv, int i, int j, int d) {
        int l;
        if(i>j) return -1;
        else {
            l=(i+j)/2;
            if(d==vv[l][1]) return l;
            else if(d<vv[l][1]) return find(vv,i,l-1,d);
            else return find(vv,l+1,j,d);
        }
    }
};

