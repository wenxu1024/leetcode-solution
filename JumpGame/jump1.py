#! /usr/bin/python

class Solution:
    # @param A, a list of integers
    # @return a boolean
    ''' Greedy algirithm'''
    def canJump(self,A):
        l = len(A)
        i = 0
        t = 0
        while i < l - 1:
            if A[i] == 0:
                return False
            else:
                maxi = -9999
                for k in range(1, A[i] + 1):
                    if i + k >= l - 1:
                        return True
                    else:
                        if i + k + A[i + k] > maxi:
                            maxi = i + k + A[i + k]
                            t = i + k
                i = t
        return True
        

if __name__ == "__main__":
    A = [2, 3, 1, 1, 4]
    B = [3, 2, 1, 0, 4]
    C = [A, B]
    sol = Solution()
    for item in C:
        print item, sol.canJump(item)
