#! /usr/bin/python

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        l = len(prices)
        if l < 2:
            return 0
        i = 0
        j = 0
        tot = 0
        state = 0 # state 0 ascending, state 1 descending
        for i in range(l - 1):
            if (prices[i + 1] < prices[i]) and (state == 0):
                tot += (prices[i] - prices[j])
                state = 1
            elif (prices[i + 1] > prices[i]) and (state == 1):
                j = i
                state = 0
        if (prices[l - 1] > prices[j]) and (state == 0):
            tot += (prices[l - 1] - prices[j])
        return tot
        

if __name__ == "__main__":
    prices = [3, 5, 1, 4, 8, 6, 9]
    sol = Solution()
    print sol.maxProfit(prices)
   
