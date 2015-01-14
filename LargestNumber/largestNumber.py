#! /usr/bin/python 

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted(num, key = self.strstr, reverse = True)
        l = len(num)
        if num[0] == 0:
            return '0'
        res = ''
        for item in num:
            res = res + str(item)
        return res
        
    def strstr(self, item):
        return 100*str(item)
        

if __name__ == "__main__":
    sol = Solution()
    num = [3, 30, 34, 5, 9]
    print sol.largestNumber(num)
