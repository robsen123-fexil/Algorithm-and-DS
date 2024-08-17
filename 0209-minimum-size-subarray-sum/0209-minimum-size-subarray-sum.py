class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        hsh={0:-1}
        sums=0
        minima=float('inf')
        l=0
        for i , val in enumerate(nums):
            sums+=val
            while sums>=target:
                res=i-l+1
                minima=min(minima , res)
                sums-=nums[l]
                l+=1
        return minima if minima!=float('inf') else 0