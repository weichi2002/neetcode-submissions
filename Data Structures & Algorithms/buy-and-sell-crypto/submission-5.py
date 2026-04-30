class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxP = 0
        
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            maxP = max(maxP, profit)




        
        return maxP
