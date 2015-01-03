#! /usr/bin/python

class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = ''
        d = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',
             15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',0:'Z'}
        q = num
        l = []
        while q != 0:
            r = q % 26
            l.append(d[r])
            if r == 0:
                q = (q - 26) / 26
            else:
                q = (q - r) / 26
        n = len(l)
        for i in range(n - 1, -1, -1):
            res += l[i]
        return res
        
        
            
if __name__ == "__main__":
    sol = Solution()
    num = 112000000000000
    print sol.convertToTitle(num)
