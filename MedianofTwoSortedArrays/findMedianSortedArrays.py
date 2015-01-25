#! /usr/bin/python

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        i = 0
        j = m - 1
        s = 0
        t = n - 1
        if (m + n) % 2 == 0:
            r1 = (m + n) / 2
            r2 = r1 + 1
            median = (self.findRankr(A, B, i, j, s, t, r1) + self.findRankr(A, B, i, j, s, t, r2)) / 2.0
        else:
            r1 = (m + n) / 2 + 1
            median = self.findRankr(A, B, i, j, s, t, r1) / 1.0
        return median
        
    def findRankr(self, A, B, i, j, s, t, r):
        if i == j + 1:
            return B[s + r - 1]
        elif s == t + 1:
            return A[i + r - 1]
        else:
	    if r == 1:
                return min(A[i], B[s])  # if rank is 1, return the minimum of A, B
            m = j - i + 1
            n = t - s + 1
            k = r * m / (m + n) # else divide r according to the lenght of A, B
	    if k == 0:
                k += 1 # keep at least one element in A selected for compare
            l = r - k
            if A[i + k - 1] == B[s + l - 1]:
                return A[i + k - 1] # if kth element in A, equal lth element in B, then A[i + k - 1] is the answer 
            elif A[i + k - 1] < B[s + l - 1]:
                return self.findRankr(A, B, i + k, j, s, t, r - k) # if smaller, rank r can't be in 0..k-1 part of A
            else:
                return self.findRankr(A, B, i, j, s + l, t, r - l) # if larger, rank r can't be in 0..l -1 part of B
            

if __name__ == "__main__":
    A = [1]
    B = [1, 2]
    sol = Solution()
    print sol.findMedianSortedArrays(A, B)
