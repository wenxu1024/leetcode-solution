#! /usr/bin/python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        l=len(A)
        for i in range(1,l+1):
            if i not in A:
                return i
        return l+1

if __name__=="__main__":
    s=Solution()
    A=[0,1,3,4,5]
    print s.firstMissingPositive(A)
