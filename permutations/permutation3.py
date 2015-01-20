#! /usr/bin/python 

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        num = [str(i + 1) for i in range(n)]
        res = self.permute(num, k - 1)
        s = ''
        for c in res:
            s = s + c
        return s
        
        
        
    def permute(self, num, k):
        if k == 0:
            return num
        l = len(num)
        i = k / self.fac(l - 1)
        j = k % self.fac(l - 1)
        r = self.permute(num[:i] + num[i + 1: ], j)
        res = [num[i]] + r
        return res
        
        
    def fac(self, i):
        f = 1
        for j in range(1, i + 1):
            f *= j
        return f


if __name__ == "__main__":
    sol = Solution()
    n = 9
    k = 4
    print sol.getPermutation(n, k)
   
