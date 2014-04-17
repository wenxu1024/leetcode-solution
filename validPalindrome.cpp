class Solution {
public:
    bool isPalindrome(string s) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        string s1,s2;
        int i,n;
        n=s.size();
        s1="";
        if(n==0) return true;
        for(i=0;i<n;i++) {
            if(s[i]>='0'&&s[i]<='9'||s[i]>='a'&&s[i]<='z'||s[i]>='A'&&s[i]<='Z') {
                if(s[i]>='A'&&s[i]<='Z') s1+=(s[i]-'A'+'a');
                else s1+=s[i];
            }
        }
        s2="";
        n=s1.size();
        for(i=0;i<n;i++) s2+=s1[n-1-i];
        if(s1==s2) return true;
        else return false;
    }
};
