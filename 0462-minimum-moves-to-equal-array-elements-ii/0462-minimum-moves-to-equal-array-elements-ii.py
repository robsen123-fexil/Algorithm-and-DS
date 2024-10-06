class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        sums=0
        nums.sort()
        while l<=r:
            sums+=abs((nums[r]-nums[l]))
            l+=1
            r-=1
        return sums
