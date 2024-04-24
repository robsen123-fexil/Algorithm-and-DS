class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        first=nums[0]
        minimal=float('inf')
        for i in range(1, len(nums)):
            first|=nums[i]
        if first<k :
            return -1
        def binmal(nums):
            checker=nums[0]
            for i in range(1, len(nums)):
                
                checker|=nums[i]
            return checker 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                
                s=nums[i:j]
                
                
                if binmal(s)>=k:
                    l=len(s)


                    minimal=min(minimal , l)
        return minimal      
                