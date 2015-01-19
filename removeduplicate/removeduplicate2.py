#! /usr/bin/python

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        l = len(A)
        if l < 3:
            return l
        i = 0
        j = 1
        c = 1
        for j in range(1, l):
            if A[j] == A[i]:
                c += 1
            else:
                if c >= 2:
                    A[i + 1] = A[i]
                    i += 2
                else:
                    i += 1
                A[i] = A[j]
                c = 1
                
        if c == 1:
            return i + 1
        if c >= 2:
            A[i + 1] = A[i]
            return i + 2
                
                    
            
            
if __name__ == "__main__":
    A = [1, 1, 1, 3, 3]
    sol = Solution()
    l = sol.removeDuplicates(A)
    print A[:l]
