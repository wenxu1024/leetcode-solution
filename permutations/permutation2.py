#! /usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        d = {}
        l = len(num)
        if l == 1:
            return [num]
        res = []
        resl = []
        for i in range(l):
            if num[i] not in d:
                d[num[i]] = True
                num[0], num[i] = num[i], num[0]
                resl = self.permuteUnique(num[1:])
                for item in resl:
                    res.append([num[0]] + item)
                num[0], num[i] = num[i], num[0]
        return res


if __name__ == "__main__":
    num = [1,1,2]
    sol = Solution()
    print sol.permuteUnique(num)
