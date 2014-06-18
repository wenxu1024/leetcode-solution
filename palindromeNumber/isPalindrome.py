#! /usr/bin/python
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        x=abs(x)
        s=str(x)
        l=len(s)
        stack=[]
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1]==c:
                    stack.pop()
                else:
                    stack.append(c)
        if not stack:
            return True   # length is even
        stack=[]
        for i in range(l):
            if i==l/2:
                continue
            else:
                if not stack:
                    stack.append(s[i])
                else:
                    if stack[-1]==s[i]:
                        stack.pop()
                    else:
                        stack.append(s[i]) # lenght is odd
        if not stack:
            return True
        return False
        
if __name__=='__main__':
     sol=Solution()
     x=1234567654321
     print sol.isPalindrome(x)
