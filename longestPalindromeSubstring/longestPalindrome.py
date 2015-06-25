#! /usr/bin/python
            

                   
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l = len(s)
        stemp = s[::-1]
        for i in range(l, 0 , -1):
            for j in range(0, l - i + 1):
                if s[j : j + i] == stemp[l - j - i : l - j]:
                    return s[j : j + i]
                    
             
            



if __name__ == "__main__":
    s = "abcba"
    sol = Solution()
    print sol.longestPalindrome(s)
