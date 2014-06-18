#! /usr/bin/python
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack=[]
        l=len(s)
        for i in range(l):
            if not stack:
                stack.append((s[i],i))
            else:
                if stack[-1][0]=='(' and s[i]==')':
                    stack.pop()
                else:
                    stack.append((s[i],i))
        if not stack: # if the stack is empty, it means the whole parenthesis is valid
            return l
        bpoint=[]
        for item in stack: #obtain the position of invalid parenthesis and divide the string into valid regions
            bpoint+=[item[1]]
        bpoint=[-1]+bpoint
        bpoint+=[l]
        n=len(bpoint)
        maxl=0
        for i in xrange(1,n):
            currlen=bpoint[i]-bpoint[i-1]-1
            if currlen>maxl:
                maxl=currlen
        return maxl
            
                
if __name__=='__main__':
     sol=Solution()
     s='())()(()(())))()))()))'
     print sol.longestValidParentheses(s)
