#! /usr/bin/python

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        j=0
        l=len(A)
        count=1
        for i in range(1,l):
            if A[i]==A[j]:
		A[j+1]=A[i]
                count=count+1
            else:
                if count>=2:
                    j=j+2
                else:
                    j=j+1
                A[j]=A[i]
                count=1
        if count>=2:
            return j+2
        else:
            return j+1

if __name__=="__main__":
     A=[[],[1],[1,1,2],[1,1,1,2,2,3,3,3],[1,2,2,2,2,3],[1,1,1,1,1,1,1,2,3,3,3,3]]
     s=Solution()
     for B in A:
        print B
        l=s.removeDuplicates(B)
        C=B[:l]
        print C
