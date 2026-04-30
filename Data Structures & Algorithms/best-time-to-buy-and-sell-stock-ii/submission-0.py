class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we generally just want to buy when its profitable
        #we are no bounded by just 1 trade
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        
        return profit