#! /usr/bin/python
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=0
        l=len(A)
	if l==0:
	    return 0
        for j in range(l):
            if A[j]==A[i]:
                continue
            else:
                i=i+1
                A[i]=A[j]
        return i+1
                

if __name__=='__main__':
    s=Solution()
    A=[1,1,2]
    l=s.removeDuplicates(A)
    B=[A[i] for i in range(l)]
    print B
