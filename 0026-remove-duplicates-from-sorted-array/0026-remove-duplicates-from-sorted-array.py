class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        # for i in range(1 , len(nums)):
        #     if nums[i-1]!=nums[i]:
        #         l+=1
        #         nums[i]=nums[l]
        # return l
        r=1
        while r<len(nums):
            if nums[r]!=nums[r-1]:
                
                nums[l]=nums[r]
                l+=1
            r+=1
        return l        