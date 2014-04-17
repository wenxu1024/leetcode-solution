class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int C[10];
        int i,j,k,l,m;
        for(i=0;i<9;i++) {
            for(k=1;k<=9;k++) C[k]=0;
            for(j=0;j<9;j++) {
                if(board[i][j]>='1'&&board[i][j]<='9')
                C[board[i][j]-'0']++;
            }
            for(k=1;k<=9;k++) {if(C[k]>1) return false;}
        }
        
        for(j=0;j<9;j++) {
            for(k=1;k<=9;k++) C[k]=0;
            for(i=0;i<9;i++) {
                if(board[i][j]>='1'&&board[i][j]<='9')
                C[board[i][j]-'0']++;
            }
            for(k=1;k<=9;k++) {if(C[k]>1) return false;}
        }
        
        for(i=0;i<3;i++) {
            for(j=0;j<3;j++) {
                for(k=1;k<=9;k++) C[k]=0;
                for(l=0;l<3;l++) {
                    for(m=0;m<3;m++) {
                        if(board[3*i+l][3*j+m]>='1'&&board[3*i+l][3*j+m]<='9')
                        C[board[3*i+l][3*j+m]-'0']++;
                    }
                }
                for(k=1;k<=9;k++) {if(C[k]>1) return false;}
            }
        }
        return true;
    }
};
