class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=1
        sums=0
        while r<len(nums):
            mini=min(nums[l] , nums[r])
            print(nums[l] , nums[r])
            sums+=mini
            l+=2
            r+=2
        return sums
