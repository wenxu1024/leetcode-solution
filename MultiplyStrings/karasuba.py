#! /usr/bin/python

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return self.strassen(num1, num2)


    def padwithzeros(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        k = 1
        while k < max(l1, l2):
            k *= 2
        return ((k - l1) * '0' + num1, (k - l2) * '0' + num2)

    def strassen(self, num1, num2):
        (num1, num2) = self.padwithzeros(num1, num2)
        l = len(num1)
        if l == 1:
            return str(int(num1) * int(num2))
        else:
            a = num1[:l / 2]
            b = num1[l / 2:]
            c = num2[:l / 2]
            d = num2[l / 2:]
            ac = self.strassen(a, c)
            bd = self.strassen(b, d)
            aplusb = self.add(a, b)
            cplusd = self.add(c, d)
            aplusbxcplusd = self.strassen(aplusb, cplusd)
            adplusbc = self.substract(self.substract(aplusbxcplusd, ac), bd)
            bd = (l - len(bd)) * '0' + bd
            adplusbc = adplusbc + ((l / 2) * '0')
            acconcatenatebd = ac + bd
            res = self.add(acconcatenatebd, adplusbc)
            k = 0
            for c in res:
                if c != '0':
                    break
                else:
                    k += 1
            return res[k:]


    def add(self, num1, num2):
        carry = 0
        res = ''
        rnum1 = num1[::-1]
        rnum2 = num2[::-1]
        l1 = len(rnum1)
        l2 = len(rnum2)
        l = min(l1, l2)
        for i in range(l):
            d1 = int(rnum1[i])
            d2 = int(rnum2[i])
            if d1 + d2 + carry >= 10:
                d = d1 + d2 +carry - 10
                res += str(d)
                carry = 1
            else:
                d = d1 + d2 + carry
                res += str(d)
                carry = 0
        if l1 == l2:
            if carry == 1:
                res += str(1)
        elif l1 > l2:
            for i in range(l, l1):
                d1 = int(rnum1[i])
                if d1 + carry >= 10:
                    d = d1 + carry - 10
                    res += str(d)
                    carry = 1
                else:
                    d = d1 + carry
                    res += str(d)
                    carry = 0
            if carry == 1:
                res += str(1)
        else:
            for i in range(l, l2):
                d2 = int(rnum2[i])
                if d2 + carry >= 10:
                    d = d2 + carry - 10
                    res += str(d)
                    carry = 1
                else:
                    d = d2 + carry
                    res += str(d)
                    carry = 0
            if carry == 1:
                res += str(1)
        return res[::-1]



    def substract(self, num1, num2):
        borrow = 0
        borrow = 0
        res = ''
        rnum1 = num1[::-1]
        rnum2 = num2[::-1]
        l2 = len(rnum2)
        l1 = len(rnum1)
        l = min(l1, l2)
        for i in range(l):
            d1 = int(rnum1[i])
            d2 = int(rnum2[i])
            if d1 - borrow >= d2:
                d = d1 - borrow - d2
                res += str(d)
                borrow = 0
            else:
                d = d1 + 10 - borrow - d2
                res += str(d)
                borrow = 1
        for i in range(l, l1):
            d1 = int(rnum1[i])
            if d1 - borrow >= 0:
                d = d1 - borrow
                res += str(d)
                borrow = 0
            else:
                d = d1 + 10 - borrow
                res += str(d)
                borrow = 1
        res = res[::-1]
        k = 0
        for c in res:
            if c != '0':
                break
            else:
                k += 1
        return res[k:]
        
        
 


if __name__ == "__main__":
    num1 = "85125880314"
    num2 = "27686605178074290300912620672246135797404233852805898370339774487176828461858259960898043021481"
    sol = Solution()
    print sol.multiply(num1, num2)
	
