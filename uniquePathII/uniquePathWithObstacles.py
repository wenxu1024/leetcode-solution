#! /usr/bin/python

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        F=[[0 for j in range(n)] for i in range(m)]
        if obstacleGrid[0][0]==0:
            F[0][0]=1
        else:
            F[0][0]=0
        for j in xrange(1,n,1):
            if obstacleGrid[0][j]==1:
                F[0][j]=0
            else:
                if obstacleGrid[0][j-1]==0:
                    F[0][j]=F[0][j-1]
                else:
                    F[0][j]=0
        for i in xrange(1,m,1):
            if obstacleGrid[i][0]==1:
                F[i][0]=0
            else:
                if obstacleGrid[i-1][0]==0:
                    F[i][0]=F[i-1][0]
                else:
                    F[i][0]=0
        for i in xrange(1,m,1):
            for j in xrange(1,n,1):
                if obstacleGrid[i][j]==1:
                    F[i][j]=0
                else:
                    if obstacleGrid[i-1][j]==0 and obstacleGrid[i][j-1]==0:
                        F[i][j]=F[i-1][j]+F[i][j-1]
                    elif obstacleGrid[i-1][j]==0 and obstacleGrid[i][j-1]!=0:
                        F[i][j]=F[i-1][j]
                    elif obstacleGrid[i-1][j]!=0 and obstacleGrid[i][j-1]==0:
                        F[i][j]=F[i][j-1]
                    else:
                        F[i][j]=0
        return F[m-1][n-1]
        

if __name__=="__main__":
    s=Solution()
    obstacles=[[0,0,0,0,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,0,0,0,0,0]]
    print s.uniquePathsWithObstacles(obstacles) 
