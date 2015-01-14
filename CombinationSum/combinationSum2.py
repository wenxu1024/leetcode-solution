#! /usr/bin/python

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        if candidates == [] and target != 0:
            return []
        if candidates == [] and target == 0:
            return [[]]
        if target < 0:
            return []
        if target == 0:
            return [[]]
        candidates.sort()
        res = self.combinationSum2(candidates[:-1], target)
        res2 = self.combinationSum2(candidates[:-1], target - candidates[-1])
        for item in res2:
            res.append(item + [candidates[-1]])
        d = {}
        for item in res:
            if tuple(item) not in d:
                d[tuple(item)] = True
        fres = []
        for key in d:
            fres.append(list(key))
        return fres
            
            

if __name__ == "__main__":
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print sol.combinationSum2(candidates, target)
