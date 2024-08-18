class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        minima=float('inf')
        mu=1
        l=count=0
        for i in range(len(nums)):
            mu*=nums[i]
            while mu>=k and l<=i:
                mu=mu//nums[l]
                l+=1
            count+=(i-l+1)
        return count
