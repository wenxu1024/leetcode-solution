#! /usr/bin/python

class Solution:
    # @param A, a list of integers
    # @return an integer
    ''' Greedy algorithm, select the maximum j + A[j] in the positions accessible from i'''
    def jump(self, A):
        l = len(A)
        if l < 2:
            return 0
            
        i = 0
        n = 0
        t = 0
        while i < l - 1:
            maxi = -9999
            n += 1
            for k in range(A[i] + 1):
                if i + k >= l - 1:
                    return n
                else:
                    if i + k + A[i + k] > maxi:
                        maxi = i + k + A[i + k]
                        t = i + k
            i = t
        return n
                        
                        
                    

if __name__ == "__main__":
     A = [2, 3, 1, 1, 4]
     sol = Solution()
     print sol.jump(A)
