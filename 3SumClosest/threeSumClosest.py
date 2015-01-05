#! /usr/bin/python

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        l = len(num)
        d = 99999
        res = 0
        for i in range(l - 2):
            x = num[i]
            start = i + 1
            end = l - 1
            while start < end:
                y = num[start]
                z = num[end]
                if x + y + z == target:
                    return target
                elif x + y + z > target:
                    if x + y + z - target < d:
                        d = x + y + z - target # if difference is smaller
                        res = (x + y + z) # record x + y + z
                    end = end - 1 # decrease the sum
                else:
                    if target - (x + y + z) <d:
                        d = target - (x + y + z) # if difference is smaller
                        res = x + y + z # record the difference
                    start = start + 1 # increase the sum
        return res


if __name__ == "__main__":
    num = [-1, 2, 1, -4]
    target = 3
    sol = Solution()
    print sol.threeSumClosest(num, target)
