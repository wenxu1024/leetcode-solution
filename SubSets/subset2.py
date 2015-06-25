#! /usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        return self.recursivesubsetsWithDup(S)
        
    def recursivesubsetsWithDup(self,S):
        l = len(S)
        d = {}
        res = []
        if l == 0:
            return [[]]
        resl = self.recursivesubsetsWithDup(S[1:])
        for item in resl:
            d[tuple(item)] = True
            res.append(item)
        for item in resl:
            if tuple([S[0]] + item) not in d:
                res.append([S[0]] + item)
        return res
            

if __name__ == "__main__":
     S = [1, 2, 2]
     sol = Solution()
     print S
     print sol.subsetsWithDup(S)

