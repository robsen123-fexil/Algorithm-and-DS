class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        first=count=0
        sums=sum(nums)
        for i in nums[:-1]:
            first+=i
            sums-=i
            if first>=sums:
                count+=1
        return count
