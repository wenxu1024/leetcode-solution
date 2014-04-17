class Solution {
public:
    int candy(vector<int> &ratings) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n,i,min,mp,sum,max;
        vector<int> v;
        vector<int> posrat;
        vector<vector<int> > vposrat;
        n=ratings.size();
        for(i=0;i<n;i++) v.push_back(1);//each child has at least 1 candy
        
            for(mp=0;mp<n;mp++) {
            if(mp==0) {
                if(ratings[mp]>ratings[mp+1]) v[mp]=v[mp+1]+1;
            }
            if(mp==n-1) {
                if(ratings[mp]>ratings[mp-1]) v[mp]=v[mp-1]+1;
            }
            else {
                if(ratings[mp]>ratings[mp-1]&&ratings[mp]<=ratings[mp+1]) v[mp]=v[mp-1]+1;
                else if(ratings[mp]<=ratings[mp-1]&&ratings[mp]>ratings[mp+1]) v[mp]=v[mp+1]+1;
                else if(ratings[mp]>ratings[mp-1]&&ratings[mp]>ratings[mp+1]) {
                    max=(v[mp-1]>v[mp+1])? v[mp-1]:v[mp+1];
                    v[mp]=max+1;
                }
                else {}
                }
            }
            
            for(mp=n-1;mp>=0;mp--) {
            if(mp==0) {
                if(ratings[mp]>ratings[mp+1]) v[mp]=v[mp+1]+1;
            }
            if(mp==n-1) {
                if(ratings[mp]>ratings[mp-1]) v[mp]=v[mp-1]+1;
            }
            else {
                if(ratings[mp]>ratings[mp-1]&&ratings[mp]<=ratings[mp+1]) v[mp]=v[mp-1]+1;
                else if(ratings[mp]<=ratings[mp-1]&&ratings[mp]>ratings[mp+1]) v[mp]=v[mp+1]+1;
                else if(ratings[mp]>ratings[mp-1]&&ratings[mp]>ratings[mp+1]) {
                    max=(v[mp-1]>v[mp+1])? v[mp-1]:v[mp+1];
                    v[mp]=max+1;
                }
                else {}
                }
            }
            
        sum=0;
        for(i=0;i<n;i++) sum+=v[i]; //sum the candy each child get
        return sum;
    }
};
