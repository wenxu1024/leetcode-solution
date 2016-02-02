#! /usr/bin/python
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
	input = self.parseInput(input)
	return self.diffWaysToComputeHelper(input)

    def diffWaysToComputeHelper(self, input):
        l = len(input)
        res = []
        if l == 1:
            res += [int(input[0])]
            return res
        else:
            for i in range(l):
                if (i + 1) % 2 == 0:
                    resLeft = self.diffWaysToComputeHelper(input[:i])
                    resRight = self.diffWaysToComputeHelper(input[i + 1:])
                    op = input[i]
                    if op == '+':
                        for left in resLeft:
                            for right in resRight:
                                res += [left + right]
                    elif op == '-':
                        for left in resLeft:
                            for right in resRight:
                                res += [left - right]
                    else:
                        for left in resLeft:
                            for right in resRight:
                                res += [left * right]
            return res
            
    
    def parseInput(self, input):
        l = len(input)
        res = []
        num = ""
        for i in range(l):
            if input[i] != '+' and input[i] != '-' and input[i] != '*':
                num += input[i]
            else:
                res += [int(num)]
                res += [input[i]]
                num = ""
        if num:
            res += [int(num)]
        return res

if __name__ == "__main__":
     sol = Solution()
     input = "0+1"
     print sol.diffWaysToCompute(input)

