class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        l=len(A)
        j=0
        i=0
        while i<l:
            if A[i]==elem:
                i+=1
            else:
                A[j]=A[i]
                j+=1
                i+=1
        return j
