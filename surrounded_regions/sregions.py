#! /usr/bin/python
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m=len(board)
        if m==0:
	    return
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=='0' and i>0 and i<m-1 and j>0 and j<n-1:
                    pos=[]
                    visited=[[False for k in range(n)] for l in range(m)]
                    flag=self.dfs_visit(i,j,board,visited,pos,m,n)
		   # print flag
                    if flag:
		#	print pos
                        for p in pos:
                            board[p[0]][p[1]]='X'
        return
                    
                    
    def dfs_visit(self,i,j,board,visited,pos,m,n):
        if i<=0 or i>=m-1 or j<=0 or j>=n-1:
            return False
        if visited[i][j]==True:
            return True
        visited[i][j]=True
        pos+=[(i,j)]
        res=True
        if board[i+1][j]=='0':
            res=res and self.dfs_visit(i+1,j,board,visited,pos,m,n)
        if board[i-1][j]=='0':
            res=res and self.dfs_visit(i-1,j,board,visited,pos,m,n)
        if board[i][j+1]=='0':
            res=res and self.dfs_visit(i,j+1,board,visited,pos,m,n)
        if board[i][j-1]=='0':
            res=res and self.dfs_visit(i,j-1,board,visited,pos,m,n)
        return res

if __name__=='__main__':
    board=[['' for i in range(4)] for j in range(4)]
    board[0][0]='X'
    board[0][1]='X'
    board[0][2]='0'
    board[0][3]='X'
    board[1][0]='X'
    board[1][1]='0'
    board[1][2]='0'
    board[1][3]='X'
    board[2][0]='X'
    board[2][1]='X'
    board[2][2]='0'
    board[2][3]='X'
    board[3][0]='X'
    board[3][1]='0'
    board[3][2]='X'
    board[3][3]='X'
    print board
    s=Solution()
    s.solve(board)
    print board
