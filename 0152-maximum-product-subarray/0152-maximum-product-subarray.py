class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total = maxmul=minmul = nums[0]
        tot=float("-inf")
        for i in range(1, len(nums)):
            if nums[i]<0:
                maxmul , minmul=minmul , maxmul
                
            maxmul=max(nums[i] , nums[i]*maxmul)
            minmul=min(nums[i] , nums[i]*minmul)
            tot=max(maxmul , minmul)
            total=max(total, tot)
        return total