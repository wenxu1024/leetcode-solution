#! /usr/bin/python

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m=len(word1)
        n=len(word2)
        N=[[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(n+1):
            N[m][j]=(n-j)
        for i in range(m+1):
            N[i][n]=(m-i)
        for i in xrange(m-1,-1,-1):
            for j in xrange(n-1,-1,-1):
                if word1[i]==word2[j]:
                    N[i][j]=N[i+1][j+1]
                else:
                    N[i][j]=1+min(N[i+1][j],N[i][j+1],N[i+1][j+1])
        return N[0][0]

if __name__=="__main__":
    word1='hello'
    word2='ellop'
    s=Solution()
    print s.minDistance(word1,word2)

