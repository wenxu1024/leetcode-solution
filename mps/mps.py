#! /usr/bin/python
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
#        l = len(A)
#        maximum = -9999
#        for i in range(l):
#            c = 1
#            for j in xrange(i,l):
#                c *= A[j]
#                if c > maximum:
#                    maximum = c
#        return maximum
        l = len(A)
	if l == 1:
	     return A[0]
        Al = A[: l/2]
        Ar = A[l/2 :]
        max1 = self.maxProduct(Al)
        max2 = self.maxProduct(Ar)
        Al.reverse()
        max3 = max(self.mini(Al)*self.mini(Ar), self.maxi(Al)*self.maxi(Ar))
        return max(max1, max2, max3)
        
    def mini(self, A):
        l = len(A)
        minimum = 9999
        c = 1
        for i in range(l):
            c *= A[i]
            if c < minimum:
                minimum = c
        return minimum
    
    def maxi(self, A):
        l = len(A)
        maximum = -9999
        c = 1
        for i in range(l):
            c *= A[i]
            if c > maximum:
                maximum = c
        return maximum
        

if __name__ == '__main__':
    s = Solution() 
    A = [-4, -3, -2]
    print s.maxProduct(A)
