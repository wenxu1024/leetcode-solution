class Solution {
public:
    string countAndSay(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
int m,i,k;
string s1,s2;
char c;
s1="1";
while(n>1) {
m=s1.size();
c=s1[0];
k=0;
s2.clear();
for(i=0;i<m;i++) {
if(s1[i]==c) {
k++;
}
else {
s2+=(k+'0');
s2+=c;
c=s1[i];
k=1;
}
}
s2+=(k+'0');
s2+=c;
s1.clear();
s1+=s2;
n--;
}
return s1;
    }
};
