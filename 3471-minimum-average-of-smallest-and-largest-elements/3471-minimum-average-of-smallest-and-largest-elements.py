class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        minima=float('inf')
        l=0
        r=len(nums)-1
        while l<r:
            avg=(nums[r]+nums[l])/2
            minima=min(minima , avg)
            l+=1
            r-=1
        return minima