class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpurchase = prices[0]
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < minpurchase: minpurchase = prices[i - 1]
            if prices[i] - minpurchase > maxprofit: maxprofit = prices[i] - minpurchase
        
        return maxprofit
