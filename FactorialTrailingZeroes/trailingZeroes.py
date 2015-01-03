#! /usr/bin/python
from math import factorial
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        c = 0
        res = self.trailingZeroes(n / 2)
        while n > 0:
            c += (n + 5) / 10
            n = n / 5
        return res + c
        
        
        
        
        
if __name__ == "__main__":
    n = 721
    sol = Solution()
    print sol.trailingZeroes(n)
    print factorial(n)
