class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        # for i in nums:
        #     if i == 0:
        #         nums.append(i)
        #         nums.remove(i)
        # return nums
        l=0
        r=1
        while r<len(nums):
            if nums[l]==0:
                if nums[r]!=nums[l]:
                    nums[r] , nums[l]=nums[l] , nums[r]
                else:
                    r+=1
            else:
                l+=1
                r+=1
        print(nums)
