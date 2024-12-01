class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=r=maxima=0
        while r<len(nums):
            if nums[r]==1:
                maxima=max(maxima , r-l+1)
                r+=1
            else:
                r+=1
                l=r
            

        return maxima