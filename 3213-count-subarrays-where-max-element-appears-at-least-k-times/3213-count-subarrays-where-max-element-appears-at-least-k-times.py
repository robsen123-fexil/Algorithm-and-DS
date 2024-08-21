from collections import Counter

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        cnt = Counter()
        l = 0
        maxima=max(nums)
        
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            
            while cnt[maxima] >= k:
                count += (len(nums) - r)  # All subarrays from l to r to the end
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                l += 1
                
        return count
