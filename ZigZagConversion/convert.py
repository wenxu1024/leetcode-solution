#! /usr/bin/python

class Solution:
    # @return a string
    def convert(self, s, nRows):
        l = len(s)
        res = ""
        if nRows == 1:
            return s
        m = l / nRows  + 1
        for i in range(nRows):
            for j in range(m):
                if i == 0 or i == nRows - 1:   # if first and last row, only one char need to be added
                    if (2 * nRows - 2) * j + i < l:
                        res = res + s[(2 * nRows - 2) * j + i]
                else: # if rows in the middle, two char needs to be added
                    if (2 * nRows - 2) * j - i < l and (2 * nRows - 2) * j - i > 0:
                        res = res + s[(2 * nRows - 2) * j - i]
                    if (2 * nRows - 2) * j + i < l:
                        res = res + s[(2 * nRows - 2) * j + i]
        return res
        

if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    nRows = 3
    print sol.convert(s, nRows)

