class Solution {
public:
    bool isValid(string s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n,i;
        stack<char> st;
        n=s.size();
        for(i=0;i<n;i++) {
            if(!st.empty()) {
            if(st.top()=='('&&s[i]==')') st.pop();
            else if(st.top()=='['&&s[i]==']') st.pop();
            else if(st.top()=='{'&&s[i]=='}') st.pop();
            else st.push(s[i]);
            }
            else st.push(s[i]);
        }
        if(!st.empty()) return false;
        else return true;
    }
};
