class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minima=float('inf')
        sums=l=0
        for i in range(len(nums)):
            sums+=nums[i]
            while sums>=target:
                print(sums)
                minima=min(minima , i-l+1)
                sums-=nums[l]
                l+=1
        if minima!=float('inf'):
            return minima
        else:
            return 0