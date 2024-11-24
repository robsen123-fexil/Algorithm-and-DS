class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        mul=1
        count=l=0
        for i in range(len(nums)):
            mul*=nums[i]
            while mul>=k and i>l:
                mul//=nums[l]
                l+=1
            if mul<k:
                count+=(i-l+1)

            
        return count
