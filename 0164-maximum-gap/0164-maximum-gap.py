class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=1
        maxima=0
        while r<len(nums):
            maxima=max(maxima , nums[r]-nums[l])
            l+=1
            r+=1
        return maxima
        