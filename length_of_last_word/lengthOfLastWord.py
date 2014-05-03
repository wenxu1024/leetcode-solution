#! /usr/bin/python

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        l=len(s)
        count=0
        pos=l-1
        for i in xrange(l-1,-1,-1):
            if s[i]!=' ':
                pos=i
                break
        for j in xrange(pos,-1,-1):
            if s[j]!=' ':
                count=count+1
            else:
                break
        return count

if __name__=="__main__":
    s="Hello World"
    sol=Solution()
    print sol.lengthOfLastWord(s)

