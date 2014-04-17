class Solution {
public:
    void solveSudoku(vector<vector<char> > &board) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int i,j,m,n,k;
        int start[9][9];
        vector<int> v,pos,pos1;
        stack<vector<int> > s,s1;
        char c;
        bool B[9][9][10];
        for(i=0;i<9;i++) {
            for(j=0;j<9;j++) {
                if(board[i][j]=='.'){
                    v.push_back(i);
                    v.push_back(j);
                    s.push(v);
                    v.clear();
                }
            }
        }

        for(i=0;i<9;i++) {
            for(j=0;j<9;j++) {
                for(k=1;k<=9;k++)
                B[i][j][k]=true;
            }
        }

        while(!s.empty()) {
            pos=s.top();
            m=pos[0];
            n=pos[1];
            for(i=1;i<=9;i++) {
                c=i+'0';
                if(isValidAdd(board,m,n,c)&&B[m][n][i]) {
                    board[m][n]=c;
                    s.pop();
                    s1.push(pos);
                    B[m][n][i]=false;
                    break;
                }
            }
            if(i==10) {
                board[m][n]='.';
                for(j=1;j<=9;j++) B[m][n][j]=true;
                pos1=s1.top();
                board[pos1[0]][pos1[1]]='.';
                s1.pop();
                s.push(pos1);
            }
        }
        return;
    }


      bool isValidAdd(vector<vector<char> > &board,int m, int n, char c) {
        int i,j,a,b;
        for(i=0;i<9;i++) {if(board[i][n]==c) return false;}
        for(j=0;j<9;j++) {if(board[m][j]==c) return false;}
        a=m/3;
        b=n/3;
        for(i=0;i<3;i++) {
          for(j=0;j<3;j++) {
            if(board[3*a+i][3*b+j]==c) return false;
         }
        }
        return true;
        }
};
