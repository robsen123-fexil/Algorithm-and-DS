class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        if not nums:
            return 0
        val=count=1
        for i in range(1 , len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
            else:
                count=1
            val=max(count , val)
        return val
                
        
                
