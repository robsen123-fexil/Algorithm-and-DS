class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt=Counter()
        maxima=float('-inf')
        l=0
        for i in range(len(nums)):
            cnt[nums[i]]+=1
            while cnt[nums[i]]>k:
                cnt[nums[l]]-=1
                if cnt[nums[l]]==0:
                    cnt.pop(nums[l])
                l+=1
            
        
            maxima=max(maxima , i-l+1)
        return maxima 