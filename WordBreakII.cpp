class Solution {
public:
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        vector<string> vs,vs1;
        string prefix,postfix,s1;
        int i,n,m,j;
        n=s.size();
        if(dict.find(s)!=dict.end()) vs.push_back(s);
        for(i=1;i<=n-1;i++) {//lenth of prefix
            prefix=s.substr(0,i);
            postfix=s.substr(i,n-i);
            if(dict.find(prefix)!=dict.end()&&wbreak(s,dict)) {
                vs1=wordBreak(postfix,dict);
                m=vs1.size();
                for(j=0;j<m;j++) {
                    s1=prefix+' '+vs1[j];
                    vs.push_back(s1);
                }
            }
        }
        return vs;
    }
    
    
    bool wbreak(string s, unordered_set<string> &dict) {
                // Note: The Solution object is instantiated only once and is reused by each test case.
        int i,j,n,k;
        string substr;
        bool wb[1000][1000];
        n=s.size();
        for(i=0;i<n;i++) {
            substr=s.substr(i,1);
            if(dict.find(substr)!=dict.end()) wb[i][i]=true;
            else wb[i][i]=false;
        }
        for(i=2;i<=n;i++) {//len
            for(j=0;j<=n-i;j++) {//starting position
            substr=s.substr(j,i);
            if(dict.find(substr)!=dict.end()) wb[j][j+i-1]=true;
            else wb[j][j+i-1]=false;
                for(k=j;k<j+i-1;k++) {
                    wb[j][j+i-1]=wb[j][j+i-1]||(wb[j][k]&&wb[k+1][j+i-1]);
                }
            }
        }
        return wb[0][n-1];
    }
};
