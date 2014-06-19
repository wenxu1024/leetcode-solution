#! /usr/bin/python

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x): #Newton's method
        y0=1
        epsilon=1e-6
        while True:
            y=y0-(y0*y0-x)/(2.0*y0)
            if abs(y-y0)<epsilon:
                break
            else:
                y0=y
        return int(y)
        
if __name__=='__main__':
    sol=Solution()
    x=101
    print sol.sqrt(x)
