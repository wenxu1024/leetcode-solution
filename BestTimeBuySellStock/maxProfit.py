#! /usr/bin/python

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        l = len(prices)
        if l < 2:
            return 0
        lprices = prices[:l/2]
        rprices = prices[l/2:]
        pmin = 9999
        pmax = -9999
        for p in lprices:
            if p < pmin:
                pmin = p
        for p in rprices:
            if p > pmax:
                pmax = p
        profit = max(self.maxProfit(lprices), self.maxProfit(rprices), pmax - pmin)
        return profit
        

        

if  __name__ == "__main__":
    prices = [3, 5, 1, 4, 8, 9, 6]
    sol = Solution()
    print sol.maxProfit(prices)
   
