class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        r=1
        result=[]
        while r<len(nums):
            if nums[r]==nums[r-1]:
                nums[r-1]*=2
                nums[r]=0
            r+=1
        result=[0]*len(nums)
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                result[l]=nums[i]
                l+=1
        return result
        