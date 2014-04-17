class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        l=len(A)-1
        return self.search(A,target,0,l)
        
    def search(self,A,target,i,j):
        if i==j+1:
            return i
        else:
            k=(i+j)/2
            if target==A[k]:
                return k
            elif target>A[k]:
                return self.search(A,target,k+1,j)
            else:
                return self.search(A,target,i,k-1)
