class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(1, len(prices)):
            #if the value is lower than current l, we want to increment it 
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if prices[r] < prices[l]:
                l=r

        return res
        