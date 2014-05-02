#! /usr/bin/python

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l=len(A)
        if l==0:
            return [-1,-1]
        if target>A[l/2]:
            if self.searchRange(A[l/2+1:],target)==[-1,-1]:
                return [-1,-1]
            else:
                return [index+l/2 for index in self.searchRange(A[l/2:],target)]
        elif target<A[l/2]:
            return self.searchRange(A[:l/2],target)
        else:
            for i in xrange(l/2,-1,-1):
                if A[i]!=target:
                    break
                left=i
            for j in xrange(l/2,l,1):
                if A[j]!=target:
                    break
                right=j
            return [left,right]


if __name__=="__main__":
    A=[1,1,1,1,1,2,2,2,3,3,3,3,3]
    target=2
    s=Solution()
    print s.searchRange(A,target)
