class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        sums=0
        minindex=float('inf')
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                minindex=min(minindex , r-l+1)
                sums-=nums[l]
                l+=1 
        return 0 if minindex== float('inf') else minindex
        