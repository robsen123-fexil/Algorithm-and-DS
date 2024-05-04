class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r , maxima=0 , 1 ,0
        
        while r<len(prices):
            if prices[l] < prices[r]:
                profit=prices[r]-prices[l]
                maxima=max(maxima ,profit )
            else:
                l=r
            r+=1
        return maxima
