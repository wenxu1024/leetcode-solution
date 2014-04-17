class Solution {
public:
    string addBinary(string a, string b) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        string c;
        reverse(a);
        reverse(b);
        c=add(a,b);
        reverse(c);
        return c;
    }
    
    void reverse(string &s) {
        string s1;
        int n,i;
        n=s.size();
        for(i=n-1;i>=0;i--) {
            s1+=s[i];
        }
        for(i=0;i<n;i++) {
            s[i]=s1[i];
        }
        return;
    }
    
    string add(string a, string b) {
        int m,n,l,i,j,carry;
        string c;
        carry=0;
        m=a.size();
        n=b.size();
        l=(m<n)? m:n;
        for(i=0;i<l;i++) {
            if(a[i]-'0'+b[i]-'0'+carry<2) {c+=(a[i]-'0'+b[i]-'0'+carry+'0');carry=0;}
            else {c+=(a[i]-'0'+b[i]-'0'+carry-2+'0');carry=1;}
        }
        if(m==n) {
            if(carry==1) c+=(1+'0');
        }
        else if(m<n) {
            for(i=l;i<n;i++) {
                if(b[i]-'0'+carry<2) {c+=(b[i]-'0'+carry+'0');carry=0;}
                else {c+=(b[i]-'0'+carry-2+'0');carry=1;}
            }
            if(carry==1) c+=(1+'0');
        }
        else {
            for(i=l;i<m;i++) {
                if(a[i]-'0'+carry<2) {c+=(a[i]-'0'+carry+'0');carry=0;}
                else {c+=(a[i]-'0'+carry-2+'0');carry=1;}
            }
            if(carry==1) c+=(1+'0');
        }
        return c;
    }
};
