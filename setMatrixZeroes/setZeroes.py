#! /usr/bin/python
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m_list=[]
        n_list=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i not in m_list:
                        m_list+=[i]
                    if j not in n_list:
                        n_list+=[j]
        for i in m_list:
            for j in range(n):
                matrix[i][j]=0
        for j in n_list:
            for i in range(m):
                matrix[i][j]=0
        return

if __name__=="__main__":
     matrix=[[1,1,0,1],[0,1,1,1],[0,2,1,1],[1,1,1,1]]
     print matrix
     s=Solution()
     s.setZeroes(matrix)
     print matrix
