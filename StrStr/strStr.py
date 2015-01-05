#! /usr/bin/python

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        
        for i in range(m):
            if haystack[i] == needle[0]:
                for j in range(n):
                    if i + j >= m:
                        return -1
                    if haystack[i + j] != needle[j]:
                        break
                else:
                    return i
        return -1
                
        

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    sol = Solution()
    print sol.strStr(haystack, needle)

