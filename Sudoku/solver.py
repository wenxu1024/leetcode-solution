#! /usr/bin/python

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        l = len(board)
	pos = []
	self.terminate = False
        for i in range(l):
            for j in range(l):
                if board[i][j] == '.':
                    posi = i
                    posj = j
		    pos.append((posi, posj))
	if len(pos) == 0:
	    self.terminate = True
	    return
	(posi, posj) = pos[0]
        for k in range(1, 10):
            if self.isValid(board, posi, posj, k):
                board[posi][posj] = str(k)
                self.solveSudoku(board)
	        if self.terminate == True:	
                      break
                else:
		      board[posi][posj] = '.' # backtrack
        return

    
    def isValid(self, board, posi, posj, k):
        for i in range(9):
            if board[i][posj] == str(k):
                return False
        for j in range(9):
            if board[posi][j] == str(k):
                return False
        bi = posi / 3 #block number i
        bj = posj / 3 #block number j
        for i in range(3):
            for j in range(3):
                if board[bi * 3 + i][bj * 3 + j] == str(k):
                    return False
        return True
        

if __name__ == "__main__":
    sol = Solution()
    board = [['.','.','9','7','4','8','.','.','.'],
             ['7','.','.','.','.','.','.','.','.'],
             ['.','2','.','1','.','9','.','.','.'],
             ['.','.','7','.','.','.','2','4','.'],
             ['.','6','4','.','1','.','5','9','.'],
             ['.','9','8','.','.','.','3','.','.'],
             ['.','.','.','8','.','3','.','2','.'],
             ['.','.','.','.','.','.','.','.','6'],
             ['.','.','.','2','7','5','9','.','.']]
    print board
    sol.solveSudoku(board)
    print board
