class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        maxima=float('-inf')
        while l<=r:
            maxima=max(maxima , nums[r]+nums[l])
            l+=1
            r-=1
        return maxima
