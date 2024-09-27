class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        l=count=0
        sets=len(set(nums))
        for i in range(len(nums)):
            cnt=Counter()
            for j in range(i, len(nums)):
                cnt[nums[j]]+=1
                if len(cnt)==sets:
                    count+=1
                
                
        return count
