#! /usr/bin/python

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s): 
        l = len(s)
        C = [0 for i in range(l + 1)]
        P = [[False for j in range(l)] for i in range(l)]
        for i in range(l + 1):
            C[i] = l - i  # mincut for suffix S[i..n]
        for i in range(l):
            P[i][i] = True # bool indicating whether S[i, j] is a palindrome
            
        for i in range(l - 1):
            if s[i] == s[i + 1]:
                P[i][i + 1] = True
            else:
                P[i][i + 1] = False
        
        for length in range(3, l + 1):
            for i in range(l - length, -1, -1):
                j = length + i - 1
                if P[i + 1][j - 1] == True and s[i] == s[j]:
                    P[i][j] = True
                else:
                    P[i][j] = False
                    
        for i in range(l - 1, -1, -1):
            for j in range(l - 1, i - 1, -1):
                if P[i][j]:
                    C[i] = min(C[i], 1 + C[j + 1])
        return C[0] - 1

if __name__ == "__main__":
    s = "leet"
    sol = Solution()
    print sol.minCut(s)
