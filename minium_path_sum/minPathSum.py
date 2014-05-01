#! /usr/bin/python
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        D=[[0 for j in range(n)] for i in range(m)]
        D[m-1][n-1]=grid[m-1][n-1]
        for j in xrange(n-2,-1,-1):
            D[m-1][j]=D[m-1][j+1]+grid[m-1][j]
        for i in xrange(m-2,-1,-1):
            D[i][n-1]=D[i+1][n-1]+grid[i][n-1]
        for i in xrange(m-2,-1,-1):
            for j in xrange(n-2,-1,-1):
                D[i][j]=min(D[i+1][j],D[i][j+1])+grid[i][j]
        return D[0][0]


if __name__=="__main__":
    grid=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    s=Solution()
    print s.minPathSum(grid)
