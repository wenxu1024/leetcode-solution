class Solution {
public:
    int numDecodings(string s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int c[100000];
        int i,n,d;
        n=s.size();
        if(s[0]=='0') c[1]=0; else c[1]=1;
        if(s[1]=='0'&&s[0]=='0') c[2]=0;
        else if(s[1]!='0'&&s[0]=='0') c[2]=0;
        else if(s[1]=='0'&&s[0]!='0') {
            d=(s[0]-'0')*10+(s[1]-'0');
            if(d<=26) c[2]=1;
            else c[2]=0;
        }
        else {
            d=(s[0]-'0')*10+(s[1]-'0');
            if(d<=26) c[2]=2;
            else c[2]=1;
        }
        
        for(i=3;i<=n;i++) {
            if(s[i-2]=='0'&&s[i-1]=='0') c[i]=0;
            else if(s[i-2]=='0'&&s[i-1]!='0') c[i]=c[i-1];
            else if(s[i-2]!='0'&&s[i-1]=='0') {
                d=(s[i-2]-'0')*10+(s[i-1]-'0');
                if(d<=26) c[i]=c[i-2];
                else c[i]=0;
            }
            else {
                d=(s[i-2]-'0')*10+(s[i-1]-'0');
                if(d<=26) c[i]=c[i-1]+c[i-2];
                else c[i]=c[i-1];
            }
        }
        return c[n];
    }
};
