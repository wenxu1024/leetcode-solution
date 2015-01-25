#! /usr/bin/python

class Solution:
    # @return a string
    def minWindow(self, S, T):
        m = len(S)
        n = len(T)
        begin = 0
        end = 0
        tobefound = {}
        hasfound = {}
        for c in T:
            if c not in tobefound:
                tobefound[c] = 1
            else:
                tobefound[c] += 1
            hasfound[c] = 0
        count = 0
        if S[end] in tobefound:
            hasfound[S[end]] = 1
        for key in hasfound:
            if hasfound[key] >= tobefound[key]:
                count += tobefound[key]
        while (count < n and end < m):
            end += 1
            if end < m:
                if S[end] in tobefound:
		    hasfound[S[end]] += 1
                    if hasfound[S[end]] == tobefound[S[end]]:
                        count += tobefound[S[end]]
                
        if count < n and end == m:
            return ""
        minwindow = end - begin + 1
        res = (begin, end)
        
        while(end < m):
            window = end - begin + 1
            if window < minwindow:
                minwindow = window
                res = (begin, end)
            if S[begin] not in hasfound:
                begin += 1   # S[begin] not in T, increment begin
            else:
                if hasfound[S[begin]] > tobefound[S[begin]]:
                    begin += 1 # begin in T, but increase begin will still has enough S[begin] in T
                    hasfound[S[begin - 1]] -= 1 # decrease S[begin] count
                else:
                    end += 1 # can't increase begin, then increase end, which will not do any harm
                    if end < m:
                        if S[end] in hasfound:
                            hasfound[S[end]] += 1 #increase S[end] count
        return S[res[0]: res[1] + 1]
         

if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    sol = Solution()
    print sol.minWindow(S,T)
