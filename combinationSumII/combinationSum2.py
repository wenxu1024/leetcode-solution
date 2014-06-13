#! /usr/bin/python

 #class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
 #   def combinationSum2(self,candidates, target):
#	res=self.combinationSum(candidates,target)
#        l=len(res)
#        rest=[]
#        for i in range(l):
#	    if res[i] not in rest:
#		rest=rest+[res[i]]
#	return rest
#
#    def combinationSum(self, candidates, target):
#        candidates.sort()
#        l=len(candidates)
#        if l==0 and target==0:
#            return [[]]
#        if l==0 and target!=0:
#            return []
#        c=candidates[1:]
#        res1=self.combinationSum(c,target)
#        res2=[[candidates[0]]+lres for lres in self.combinationSum(c,target-candidates[0])]
#	res=res1+res2
#        return res 
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.combinationSum(candidates,target)
        
    def combinationSum(self,candidates,target):
        l=len(candidates)
        if l==0 and target==0:
            return [[]]
        if l==0 and target!=0:
            return []
        c=candidates[1:]
        res1=self.combinationSum(c,target)
        res2=[[candidates[0]]+lres for lres in self.combinationSum(c,target-candidates[0])]
        res=res1+res2
        l=len(res)
        rest=[]
        for i in range(l):
            if res[i] not in rest:
                rest=rest+[res[i]]
        return rest

if __name__=="__main__":
    s=Solution()
    candidates=[10,1,2,7,6,1,5]
    target=8
    print s.combinationSum2(candidates,target)

