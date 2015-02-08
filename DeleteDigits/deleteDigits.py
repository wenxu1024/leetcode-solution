#! /usr/bin/python

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        l = len(A)
        S = [['' for j in range(k + 1)] for i in range(l + 1)]
        T = ''
        for j in range(0, k + 1):
            S[j][j] = ''
        for i in range(1, l + 1):
            T += A[i - 1]
            S[i][0] = T

        for j in range(1, k + 1):
            for i in range(j + 1, l + 1):
                if self.smaller (S[i - 1][j - 1], S[i - 1][j] + A[i - 1]):
                    S[i][j] = S[i - 1][j - 1]
                else:
                    S[i][j] = S[i - 1][j] + A[i - 1]

        res = S[l][k]
        p = 0
        # remove prevailing zeros
        for i in range(len(res)):
            if res[i] != '0':
                p = i
                break
        return res[p : ]

    def smaller(self, s1, s2):
        if int(s1) < int(s2):
            return True
        else:
            return False

 



if __name__ == "__main__":
    A = "178542"
    k = 4
    sol = Solution()
    print sol.DeleteDigits(A, k)
