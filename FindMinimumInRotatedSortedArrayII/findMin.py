#! /usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l = len(num)
        return self.findindex(num, 0, l - 1)
        
    def findindex(self, num, i, j):
        if i == j:
            return num[i]
        elif i + 1 == j:
            return min(num[i], num[j])
        else:
            k = (i + j) / 2
            if num[k] > num[i]:
                return min(num[i], self.findindex(num, k + 1, j))
            elif num[k] < num[i]:
                return self.findindex(num, i, k)
            else:
                return min(num[i], self.findindex(num, k + 1, j), self.findindex(num, i, k))
        

if __name__ == '__main__':
    num = [10, 10, 1, 10, 10, 10]
    sol = Solution()
    print sol.findMin(num)
