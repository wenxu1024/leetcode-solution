#! /usr/bin/python

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        l=len(matrix)
        for i in range(l):
            for j in range(i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp #this nested for loop is for transpose matrix in place
        for j in range(l/2):
            for i in range(l):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][l-1-j]
                matrix[i][l-1-j]=temp #this nested for loop exchange column j with column n-j
        return matrix
        
if __name__=="__main__":
     s=Solution()
     matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
     print matrix
     print s.rotate(matrix)
