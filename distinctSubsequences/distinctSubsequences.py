#! /usr/bin/python

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m = len(S)
        n = len(T)
        C = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(m + 1):
            C[i][0] = 1
        for j in xrange(1, n + 1):
            C[0][j] = 0
        for i in xrange(1, m + 1):
            for j in range(1, n + 1):
                if S[i - 1] != T[j - 1]:
                    C[i][j] = C[i - 1][j]
                else:
                    C[i][j] = C[i - 1][j] + C[i - 1][j - 1]
        return C[m][n]
            

if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    sol = Solution()
    print sol.numDistinct(S, T)
