#! /usr/bin/python

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        HP =[[0 for j in range(n)] for i in range(m)]
        for j in range(n - 1, -1 , -1):
            if j == n - 1:
                if dungeon[m - 1][j] < 0:
                    HP[m - 1][j] = 1 - dungeon[m - 1][j]
                else:
                    HP[m - 1][j] = 1
            else:
                if HP[m - 1][j + 1] - dungeon[m - 1][j] < 0:
                    HP[m - 1][j] = 1
                else:
                    if HP[ m - 1][j + 1] == 0:
                        HP[m - 1][j] = 1 - dungeon[m - 1][j]
                    else:
                        HP[m - 1][j] = HP[m - 1][j + 1] - dungeon[m - 1][j]
                    
        for i in range(m - 1, -1, -1):
            if i == m - 1:
                if dungeon[i][n - 1] < 0:
                    HP[i][n - 1] = 1 - dungeon[i][n - 1]
                else:
                    HP[i][n - 1] = 1
            else:
                if HP[i + 1][n - 1] - dungeon[i][n - 1] < 0:
                    HP[i][n - 1] = 1
                else:
                    if HP[i + 1][n - 1] == 0:
                        HP[i][n - 1] = 1 - dungeon[i][n - 1]
                    else:
                        HP[i][n - 1] = HP[i + 1][n - 1] - dungeon[i][n - 1]
                        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                test = min(HP[i + 1][j], HP[i][j + 1])
                if test - dungeon[i][j]< 0:
                    HP[i][j] = 1
                else:
                    if test == 0:
                        HP[i][j] = 1 - dungeon[i][j]
                    else:
                        HP[i][j] = test - dungeon[i][j]
        return HP[0][0]
                


if __name__ == "__main__":
     sol = Solution()
     dungeon = [[2, 1], [1, -1]]
     print sol.calculateMinimumHP(dungeon)
