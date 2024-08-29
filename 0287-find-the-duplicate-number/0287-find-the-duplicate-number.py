class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=0
        nums.sort()
        r=1
        while r<len(nums):
            if nums[r]==nums[l]:
                return nums[r]
            r+=1
            l+=1