class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        mult=1
        count=l=0
        for i in range(len(nums)):
            mult*=nums[i]
            while mult>=k and i>l:
                mult//=nums[l]
                l+=1
            if mult<k:
                
                count+=(i-l+1)
        return count