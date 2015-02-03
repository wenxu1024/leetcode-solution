#! /usr/bin/python

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        l = len(prices)
        if l < 2:
            return 0
        max2p = 0
        list = [0]
        for i in range(1, l - 1):
            if prices[i] >= prices[i - 1] and prices[i] > prices[i + 1]:
                list.append(i)
        list.append(l - 1)
        for k in list:
            max2p = max(max2p, self.maxProfitHelper(prices, 0, k) + self.maxProfitHelper(prices, k, l - 1))
        return max2p
        
        
    def maxProfitHelper(self, prices, i, j):
        buy = prices[i]
        maxp = 0
        for k in range(i + 1, j + 1):
            if prices[k] > buy:
                sell = prices[k]
                maxp = max(maxp, sell - buy)
            else:
                buy = prices[k]
        return maxp

if __name__ == "__main__":
    sol = Solution() 
    prices = [4,4,6,1,1,4,2,5]
    print sol.maxProfit(prices)
