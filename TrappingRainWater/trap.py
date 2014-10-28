#! /usr/bin/python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A): 
        l = len(A)
        if l <= 1:
           return 0
        (left, right) = self.partition(A)
        Aleft = A[:left + 1]
        Aright = A[right:]
        water = self.trapsingle(A, left, right)
        water += (self.trap(Aleft) + self.trap(Aright))
        return water
    

    def partition(self, A): 
        left = 0 
        right = 0 
        l = len(A)
        maxi = -9999
        sndmaxi = maxi
        sndmaxindex = -1
        maxindex = -1
        for i in range(l):
           if A[i] >= maxi:
              sndmaxi = maxi
              sndmaxindex = maxindex
              maxi = A[i]
              maxindex = i 
           else:
              if A[i] > sndmaxi:
                 sndmaxi = A[i]
                 sndmaxindex = i 

        left = min(maxindex, sndmaxindex) 
        right =max(maxindex, sndmaxindex)
        return (left, right)


    def trapsingle(self, A, index1, index2):
       depth = min(A[index1], A[index2])
       water = 0 
       for i in xrange(index1 + 1, index2):
           if depth >= A[i]:
              water += (depth - A[i])
       return water

if __name__ == "__main__":
    sol = Solution()
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
    print sol.trap(A)

