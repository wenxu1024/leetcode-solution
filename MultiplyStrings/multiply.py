#! /usr/bin/python

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        rnum1 = num1[::-1]
        rnum2 = num2[::-1]
        carry = 0
        l1 = len(rnum1)
        l2 = len(rnum2)
        res = "0"
        for j in range(l2):
            dres = ""
            carry = 0
            for i in range(l1):
                d1 = int(rnum1[i])
                d2 = int(rnum2[j])
                k = 0
                d = d1 * d2 + carry
                while d >= 10:
                    d -= 10
                    k += 1
                dres += str(d)
                carry = k
            if carry != 0:
                dres += str(carry)
            dres = j * '0' + dres
            res = self.add(res, dres[::-1])
        k = 0
        for c in res:
            if c!= '0':
                break
            else:
                k += 1
        if res[k:] == "":
            return '0'
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


if __name__ == "__main__":
    sol = Solution()
    num1 = "999999999999"
    num2 = "888888888888"
    print sol.multiply(num1, num2)
