ass Solution {
public:
    int evalRPN(vector<string> &tokens) {
        int n;
        n=tokens.size();
        return eval(tokens,0,n-1);
    }
        
    int eval(vector<string>& tokens, int i, int j) {
        int k,l,n,v1,v2,v,np,nn;
        n=j-i+1;
        np=0;
        nn=0;
        if(n==1) return stringtovalue(tokens[i]);
        else {
            for(l=j-1;l>=i;l--) {
                if(tokens[l]=="+"||tokens[l]=="-"||tokens[l]=="*"||tokens[l]=="/") np++;
                else nn++;
                if(nn==np+1) break;
            }
                v1=eval(tokens,i,l-1);
                v2=eval(tokens,l,j-1);
                if(tokens[j]=="+") return v1+v2;
                else if(tokens[j]=="-") return v1-v2;
                else if(tokens[j]=="*") return v1*v2;
                else return v1/v2;
            }
        }
    
    int stringtovalue(string s) {
        int v,n,i;
        n=s.size();
        v=0;
        if(s[0]=='-') {
        for(i=1;i<n;i++) {
            v=v*10+(s[i]-'0');
        }
        v=-v;
        }
        else {
            for(i=0;i<n;i++) {
                v=v*10+(s[i]-'0');
            }
        }
        return v;
    }
};
