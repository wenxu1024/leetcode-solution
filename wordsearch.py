class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
          m=len(board)
          n=len(board[0])
          visited=[[0 for i in range(n)] for j in range(m)]
          for i in range(0,m):
               for j in range(0,n):
                     if    self.dfs(board,i,j,0,word,visited):
                           return True
          return False
 
    def dfs(self,board,i,j,k,word,visited):
          m=len(board)
          n=len(board[0])
          if i<0 or i>=m or j<0 or j>=n:
                return False
          if k==len(word):
                return True
          if word[k]!=board[i][j]:
                return False
          if visited[i][j]:
                return False
          visited[i][j]=True
          res=self.dfs(board,i+1,j,k+1,word,visited) or \
                 self.dfs(board,i-1,j,k+1,word,visited) or \
                 self.dfs(board,i,j+1,k+1,word,visited) or \
                 self.dfs(board,i,j-1,k+1,word,visited)
          visited[i][j]=False
          return res
                     

      
