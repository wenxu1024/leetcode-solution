#! /usr/bin/python

class Solution:
    # @return an integer
    def atoi(self, str):
        if str == '':
            return 0
        l = len(str)
        j = 0
        res = 0
        for i in range(l):
            if str[i] == ' ':
                j += 1
            else:
                break
        if str[j] == '+' or str[j] == '-':
            for i in range(j + 1, l):
                if str[i] >= '0' and str[i] <= '9':
                    res = res * 10 + int(str[i])
                else:
                    break
        elif str[j] >= '0' and str[j] <= '9':
            for i in range(j, l):
                if str[i] >= '0' and str[i] <= '9':
                    res = res * 10 + int(str[i])
                else:
                    break
        else:
            return 0
        if str[j] == '+' or (str[j] >= '0' and str[j] <= '9'):
            if res > 2147483647:
                return 2147483647
            else:
                return res
        else:
            if res > 2147483647:
                return -2147483648
            else:
                return -res
        
                
        

if __name__ == "__main__":
    str = '   +11124234'
    sol = Solution()
    print sol.atoi(str)
