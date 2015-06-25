#! /usr/bin/python
from allprime import primes

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        sign = ""
        if (numerator > 0 and denominator <0) or (numerator <0 and denominator > 0):
            sign ="-"

            
        numerator = abs(numerator)
        denominator = abs(denominator)
        remainder = numerator % denominator
        quotient = numerator / denominator
        d= {}
        res = str(quotient)
        if remainder == 0:
            return sign + res
        res += '.'
        d[remainder] = 0
        l = []
        while remainder != 0:
            numerator = remainder * 10
            quotient = numerator / denominator
            remainder = numerator % denominator
            l.append(quotient)
            if remainder in d:
                p = d[remainder]
                break
            else:
                d[remainder] = len(l)
                if remainder == 0:
                    break
        
        n = len(l)
        if remainder == 0:
            for item in l:
                res += str(item)
            return sign + res
            
        for i in range(p):
            res += str(l[i])
        res += '('
        for i in range(p,n):
            res += str(l[i])
        res += ')'
        return sign + res
        
        
if __name__ == "__main__":
    numerator = 1
    sol = Solution()
    n = 100000
    l = primes(n)
    for denominator in l:
        print denominator, len(sol.fractionToDecimal(numerator,denominator))
