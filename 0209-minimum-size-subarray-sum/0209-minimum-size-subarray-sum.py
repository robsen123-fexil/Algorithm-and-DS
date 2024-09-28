class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        sums=0
        minima=float('inf')
       
        for i , val in enumerate(nums):
            sums+=val
            while sums>=target:
                minima=min(minima , i-l+1)
                sums-=nums[l]
                l+=1
        return minima if minima!=float('inf') else 0