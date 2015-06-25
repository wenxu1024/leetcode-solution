#! /usr/bin/python
import sys
class Solution:
    ''' facebook phone interview jump river'''
    def minJump(self,R):
        l = len(R)
        if l < 2:
            return 0
        if R[0] != 1:
            return sys.maxint
        N = [[0 for j in range(2 * l)] for i in range( 2* l)]
        for j in range(2*l):
            for i in range(l,2*l):
                N[i][j] = 0
        for j in range(1, 2* l):
            N[l - 1][j] = 1
        N[l - 1][0] = 1
        for j in range(2*l - 1, -1 , -1):
            for i in range(l - 2, -1 , -1):
                if i + j + 1 >= l:
                    N[i][j] = 1
                else:
		    if j == 0:
                        if R[i + j + 1] == '0':
                             N[i][j] = sys.maxint
                        else:
                             N[i][j] = 1 + N[i + j + 1][j + 1]
                    else:
                        if R[i + j + 1] == '0' and R[i + j] == '0':
                             N[i][j] = sys.maxint
                        elif R[i + j + 1] == '1' and R[i + j] == '0':
                             N[i][j] = 1 + N[i + j + 1][j + 1]
                        elif R[i + j + 1] == '0' and R[i + j] == '1':
                             N[i][j] = 1 + N[i + j][j]
                        else:
                             N[i][j] = 1 + min(N[i + j][j], N[i + j + 1][j + 1])
	return N[0][1]


if __name__ == "__main__":
    l1 = [1, 1, 1, 0, 1, 1, 0, 0]
    l2 = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1]
    l = [l1, l2]
    sol = Solution()
    for item in l:
        print item, sol.minJump(item)
