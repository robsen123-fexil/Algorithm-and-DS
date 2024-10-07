class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums=l=0
        maxima=float('inf')
        for i in range(len(nums)):
            sums+=nums[i]
            while sums>=target:
                maxima=min(maxima , i-l+1)
                sums-=nums[l]
                l+=1
        return maxima if maxima!=float(inf) else 0