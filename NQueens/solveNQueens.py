#! /usr/bin/python

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        l = [['.' for j in range(n)] for i in range(n)]
        d = {}
        answer = []
        for i in range(n):
            d[i] = False
        self.solve(n, 0, l, d, answer)
        return answer
        
        
    def solve(self, n, i, l, d, answer):
        if i == n:
	    lres = self.convertL(l)
	    answer.append(lres)
            return
        for j in range(n):
            if d[j] == False and self.isValid(n, i, j, l, d):
                d[j] = True
                l[i][j] = 'Q'
                self.solve(n, i + 1, l, d, answer)
                l[i][j] = '.'
                d[j] = False
        return
    
    def isValid(self, n, i, j, l, d):
        for k in range(1, min(i, j) + 1):
            if l[i - k][j - k] == 'Q':
                return False
        for k in range(1, min(i, n - j - 1) + 1):
            if l[i - k][j + k] == 'Q':
                return False
        return True
 
    def convertL(self, l):
        m = len(l)
        lres = []
        for i in range(m):
             res = ''
	     for j in range(m):
                res = res + l[i][j]
             lres.append(res)
            
        return lres

if __name__ == "__main__":
     sol = Solution()
     n = 4
     print sol.solveNQueens(n)
