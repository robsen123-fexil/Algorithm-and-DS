class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxp=0
        profit=0
        for i in range(1, len(prices)):
            if prices[i]<prices[l]:
                l=i
            else:
                profit =prices[i]-prices[l]
                maxp=max(maxp , profit )
        return maxp