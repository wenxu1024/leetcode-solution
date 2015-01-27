#! /usr/bin/python

        
   
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            self.dfs_solve(board, i, 0, visited, m, n)
            self.dfs_solve(board, i, n - 1, visited, m, n)
        for j in range(n):
            self.dfs_solve(board, 0, j, visited, m, n)
            self.dfs_solve(board, m - 1, j, visited, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                else:
                    if board[i][j] == 'Y':
                        board[i][j] = 'O'
        return
        
        
    def dfs_solve(self, board, i, j, visited, m, n):
        if visited[i][j]:
            return
        if board[i][j] == 'O':
            visited[i][j] = True
            board[i][j] = 'Y'
            if i + 1 < m and board[i + 1][j] == 'O' and visited[i + 1][j] == False:
                self.dfs_solve(board, i + 1, j, visited, m, n)
            if i - 1 > 0 and board[i - 1][j] == 'O' and visited[i - 1][j] == False:
                self.dfs_solve(board, i - 1, j, visited, m, n)
            if j + 1 < n and board[i][j + 1] == 'O' and visited[i][j + 1] == False:
                self.dfs_solve(board, i, j + 1, visited, m, n)
            if j - 1 > 0 and board[i][j - 1] == 'O' and visited[i][j - 1] == False:
                self.dfs_solve(board, i, j - 1, visited, m, n)
        return
    



if __name__=='__main__':
    board=[['' for i in range(3)] for j in range(3)]
    board[0][0]='O'
    board[0][1]='O'
    board[0][2]='O'
    board[1][0]='O'
    board[1][1]='O'
    board[1][2]='O'
    board[2][0]='O'
    board[2][1]='O'
    board[2][2]='O'
    print board
    s=Solution()
    s.solve(board)
    print board
