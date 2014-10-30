#! /usr/bin/python

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        if n == 0 and m == 0:
            return True
        if n == 0 and m != 0:
            return False
            
        B = [[ False for i in range(n + 1)] for j in range(m + 1)]
        
        B[0][0] = True

        for i in xrange(0, m + 1):
            for j in xrange(1, n + 1):
                if p[j - 1] != '.' and p [j - 1] != '*':
                    if i == 0:
                        B[i][j] = False
                    else:
                        B[i][j] = B[i - 1][j - 1] and (s[i - 1] == p[j - 1])
                elif p[j - 1] == '.':
                    if i == 0:
                        B[i][j] = False
                    else:
                        B[i][j] = B[i - 1][j - 1]
                else:
                    B[i][j] = B[i][j - 2]
                    if p[j - 2] == '.':
                        for k in xrange(1, i + 1):
                            B[i][j] = B[i][j] or (B[i - k][j - 2])
                    else:
                        for k in xrange(1, i + 1):
                            B[i][j] = B[i][j] or (B[i - k][j - 2] and (s[i - k: i] == (k * p[j - 2])))
        return B[m][n]

if __name__ == "__main__":
    sol = Solution()
    print sol.isMatch("aa","a")
    print sol.isMatch("aa","aa")
    print sol.isMatch("aaa","aa")
    print sol.isMatch("aa", "a*")
    print sol.isMatch("aa", ".*")
    print sol.isMatch("ab", ".*") 
    print sol.isMatch("aab", "c*a*b") 
    print sol.isMatch("", "c*")
