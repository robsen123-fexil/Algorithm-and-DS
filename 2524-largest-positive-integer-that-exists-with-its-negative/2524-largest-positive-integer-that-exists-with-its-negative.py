class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        r=len(nums)-1
        nums.sort()
        l=0
        while l<=r:
            if nums[r]>(nums[l]*-1):
                r-=1
            elif nums[r]<(nums[l]*-1):
                l+=1
            else:
                return nums[r]
        return -1

            
