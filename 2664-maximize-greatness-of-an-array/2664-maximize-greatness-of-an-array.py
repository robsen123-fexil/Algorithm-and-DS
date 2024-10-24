class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        l=0
        r=1
        maxima=0
        count=0
        nums.sort()
        while r<len(nums):
            if nums[l]<nums[r]:
                l+=1
                count+=1
            r+=1
        return count
        