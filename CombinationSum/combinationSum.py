#! /usr/bin/python

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        if candidates == []:
            return []
        if target < 0:
            return []
        if target == 0:
            return [[]]
        candidates.sort()
        res = self.combinationSum(candidates[:-1], target)
        res2 = self.combinationSum(candidates, target - candidates[-1])
        for item in res2:
            res.append(item + [candidates[-1]])
        return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    sol = Solution()
    print sol.combinationSum(candidates, target)

