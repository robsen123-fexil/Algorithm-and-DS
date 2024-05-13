class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num=sorted(nums , reverse=True)
        n=num[1]*2
        if num[0]>=n:
            return nums.index(num[0])
        else:
            return -1      