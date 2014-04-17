class Solution {
public:
    vector<vector<string> > partition(string s) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
    vector<vector<string> > vvs,vvs1;
    vector<string> vs; 
    string s1,s2,s3;
    int i,j,k,l,n,m;
    n=s.size();
    if(n==0) {return vvs;}
    for(i=1;i<=n;i++) {
        s1=s.substr(0,i);
        s2=string(s1.rbegin(),s1.rend());
        if(s1==s2) {
            s3=s.substr(i,n-i);
            vvs=partition(s3);
            m=vvs.size();
            for(l=0;l<m;l++) {
                vvs[l].insert(vvs[l].begin(),s1);
                vvs1.push_back(vvs[l]);
            }   
            if(s1==s) {vs.clear(),vs.push_back(s);vvs1.push_back(vs);}
        }   
    }   
    return vvs1;
    } 
};
