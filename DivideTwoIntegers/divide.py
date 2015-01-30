#! /usr/bin/python

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            sign = '+'
        else:
            sign = '-'
        dividend = abs(dividend)

        divisor = abs(divisor)
            
        if dividend < divisor:
            return 0
        res = 0
        while dividend >= divisor:
            temp = divisor
            tempres = 1
            if dividend == temp:
                res += 1
                break
            else:
                while dividend > temp:
                    temp <<= 1
                    tempres <<= 1
                temp >>= 1
                tempres >>= 1
                dividend = dividend - temp
                res += tempres
        if sign == '+':
            if res == 2147483648:
                return 2147483647
            return res
        else:
            
            return -res

if __name__ == "__main__":
    divident = -2147483648
    divisor = -1
    sol = Solution()
    print sol.divide(divident, divisor)
    print divident / divisor
    
