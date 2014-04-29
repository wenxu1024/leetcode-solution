#! /usr/bin/python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        l=len(num)
        if l==1:
            return [num]
        else:
            reslist=[]
            for i in range(l):
                num_i=num[:i]+num[i+1:]
                outlist=self.permute(num_i)
                rlist=[[num[i]]+lis for lis in outlist]
                reslist=reslist+rlist
        return reslist

if __name__=="__main__":
    s=Solution()
    num=[1,2,3,4,5,6]
    print s.permute(num)
