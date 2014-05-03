#! /usr/bin/python

class Solution:
    # @param A, a list of integers
    # @return a boolean
#    def canJump(self, A):
#        l=len(A)
#        if l==1:
#            return True
#        B=[False for i in range(l)]
#        B[l-1]=True
#        for i in xrange(l-2,-1,-1):
#            for j in xrange(1,A[i]+1,1):
#                B[i]=B[i] or B[i+j]
#        return B[0]

#    def canJump(self,A):
#	maxCover=0
#        start=0
#	l=len(A)
#       while start<=maxCover and start<l:
#		if A[start]+start>maxCover:
#			maxCover=A[start]+start
#		if maxCover>=l-1:
#			return True
#	return False '''

     def canJump(self,A):
	i=0
	while i<len(A)-1:
		if A[i]==0:
			return False
		i+=A[i]
	return i>=len(A)-1
	

if __name__=="__main__":
    A=[[1,2],[3,2,1,0,4],[2,3,1,1,4],[1,1,1,1,1],[1],[4],[3,2,2,0,4],[5,6,0,0,0,0,0]]
    s=Solution()
    for C in A:
	print s.canJump(C)
	
    
