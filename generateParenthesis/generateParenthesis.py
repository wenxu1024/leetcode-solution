#! /usr/bin/python
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n==0:
            return ['']
        else:
            reslist=[]
            for i in range(n):
                reslist_l=self.generateParenthesis(i)
                reslist_r=self.generateParenthesis(n-1-i)
                rlist=['('+rlist_l+')'+rlist_r for rlist_l in reslist_l for rlist_r in reslist_r]
                reslist=reslist+rlist
            return reslist

if __name__=='__main__':
     s=Solution()
     print s.generateParenthesis(3)
     print s.generateParenthesis(4)

