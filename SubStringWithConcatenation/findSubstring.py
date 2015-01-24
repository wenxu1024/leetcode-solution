#! /usr/bin/python

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        lengthL = len(L)
        if lengthL == 0:
            return []
        lengthLItem = len(L[0])
        totalLength = lengthL * lengthLItem
        d = {}
        res = []
        for item in L:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        lengthS = len(S)
        for i in range(0, lengthS - totalLength + 1):
            dcopy = dict(d)
            str = ""
            for j in range(i, i + totalLength):
                if ((j - i) + 1) % lengthLItem != 0:
                    str = str + S[j]
                else:
                    str = str + S[j]
                    if str in dcopy:
                        dcopy[str] -= 1
	                str = ""
                    else:
                        break
            else:
                for key in dcopy:
                    if dcopy[key] != 0:
                        break
                else:
                    res.append(i)
        return res
        

if __name__ == "__main__":
     S = "barfoothefoobarman"
     L = ["foo", "bar"]
     sol = Solution()
     print sol.findSubstring(S, L)

