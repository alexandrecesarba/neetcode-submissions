class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        window_profit = 0
        cur_max = 0
        while r < len(prices):
            window_profit = prices[r] - prices[l]
            can_grow = window_profit > 0 
            if can_grow:
                cur_max = max(cur_max, window_profit)
           
            else:
                l = r
            
            r += 1
            
    
        return cur_max
        


