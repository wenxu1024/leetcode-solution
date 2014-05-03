#! /usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        C=[0 for i in range(100000)]
        l=len(num)
        D=[0 for i in range(l)]
        for i in range(l):
            C[num[i]]=C[num[i]]+1
        S=[0 for i in range(100000)]
        S_init=0
        for i in range(100000):
            S_init=S_init+C[i]
            S[i]=S_init
        for i in xrange(l-1,-1,-1):
            D[S[num[i]]-1]=num[i]
            S[num[i]]=S[num[i]]-1
	count=1
	maxcount=1
        for i in xrange(1,l,1):
            if D[i]==D[i-1]+1:
		count=count+1
	    else:
		if count>maxcount:
			maxcount=count
		count=1
	return max(count,maxcount)

if __name__=="__main__":
    num=[100,4,101,1,3,2,102,104,103,105,106]
    print num
    s=Solution()
    print s.longestConsecutive(num)
