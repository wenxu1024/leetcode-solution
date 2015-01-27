#! /usr/bin/python

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        return self.spiralOrderhelper(matrix, 0, m, 0, n)
        
    def spiralOrderhelper(self, matrix, rowlow, rowhigh, columnlow, columnhigh): #helper function
        res = []
        if rowlow >= rowhigh or columnlow >= columnhigh:
            return [] # if row or column empty, return empty list
        if rowlow + 1 == rowhigh: # if just one row, return the row
            for j in range(columnlow, columnhigh):
                res.append(matrix[rowlow][j])
            return res
        if columnlow + 1 == columnhigh: # if just one column, return the column
            for i in range(rowlow, rowhigh):
                res.append(matrix[i][columnlow])
            return res
        for j in range(columnlow, columnhigh): # get upper border
            res.append(matrix[rowlow][j])
        for i in range(rowlow + 1, rowhigh): # get right border
            res.append(matrix[i][columnhigh -1])
        for j in range(columnhigh - 2, columnlow - 1, -1): # get bottom border
            res.append(matrix[rowhigh - 1][j])
        for i in range(rowhigh - 2, rowlow, -1): # get left border
            res.append(matrix[i][columnlow])
        res = res + self.spiralOrderhelper(matrix, rowlow + 1, rowhigh - 1, columnlow + 1, columnhigh - 1) # append the inside spiral
        return res

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print sol.spiralOrder(matrix)
