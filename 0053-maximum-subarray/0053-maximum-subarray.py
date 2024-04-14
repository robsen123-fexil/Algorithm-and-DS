class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=sums=nums[0]
        for i in nums[1:]:
            sums=max(i , i+sums)
            total=max(sums , total)
        return total