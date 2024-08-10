class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i , val in enumerate(nums):
            leftsum=sum(nums[:i])
            rightsum=sum(nums[i+1:])
            if leftsum==rightsum:
                return i
        return -1
        