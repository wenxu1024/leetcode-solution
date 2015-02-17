#! /usr/bin/python

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        d = {'2' : ['a','b','c'], '3':['d','e','f'],'4':['g','h','i'],
             '5': ['j','k','l'], '6': ['m','n','o'], '7':['p','q','r','s'],
             '8': ['t', 'u', 'v'], '9':['w','x','y','z'], '0':[' ']}
        l = len(digits)
        if l == 0:
            return [""]
        res = d[digits[0]]
        for i in range(1,l):
            res = self.crossproduct(res, d[digits[i]])
        return res
        
        
    def crossproduct(self, l1 , l2):
        m = len(l1)
        n = len(l2)
        l = []
        for i in range(m):
            for j in range(n):
                l.append(l1[i] + l2[j])
        return l


if __name__ == "__main__":
    digits = "9797395652"
    sol = Solution()
    print sol.letterCombinations(digits)

