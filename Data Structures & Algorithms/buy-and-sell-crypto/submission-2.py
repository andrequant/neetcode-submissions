class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        for i in range(len(prices)):
            p = prices[i] - min(prices[:i+1])
            if p > mp:
                mp = p
        return mp

            
            
