#! /usr/bin/python

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        m=len(s)
        n=len(p)
        B=[[False for j in range(n+1)] for i in range(m+1)]

        B[m][n]=True
        
        for i in xrange(m-1,-1,-1):
            for j in xrange(n-1,-1,-1):
                if p[j]!='*' and p[j]!='?':
                    if p[j]!=s[i]:
                        B[i][j]=False
                    else:
                        B[i][j]=B[i+1][j+1]
                elif p[j]!='*' and p[j]=='?':
                    B[i][j]=B[i+1][j+1]
                else:
                    B[i][j]=False
                    for k in xrange(i,m+1,1):
                        B[i][j]=B[i][j] or B[k][j+1]
        return B[0][0]            
        

if __name__=="__main__":
    sol=Solution()
    s_list=["aa","aa","aaa","aa","aa","ab","aab","aaaabaabaabbbabaabaabbbbaabaaabaaabbabbbaaabbbbbbabababbaabbabbbbaababaaabbbababbbaabbbaabbaaabbbaabbbbbaaaabaaabaabbabbbaabababbaabbbabababbaabaaababbbbbabaababbbabbabaaaaaababbbbaabbbbaaababbbbaabbbbb"]
    p_list=["a","aa","aa","*","a*","?*","c*a*b","**a*b*b**b*b****bb******b***babaab*ba*a*aaa***baa****b***bbbb*bbaa*a***a*a*****a*b*a*a**ba***aa*a**a*"]
    l=len(s_list)
    for i in range(l):
	print sol.isMatch(s_list[i],p_list[i])
