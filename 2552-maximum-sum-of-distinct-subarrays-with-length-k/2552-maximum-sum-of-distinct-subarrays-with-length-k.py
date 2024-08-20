class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res=nums[:k]
        sums=sum(res)
        cnt=Counter(nums[:k])
        l=0
        maxima=float('-inf')
        if len(cnt)==k:
            maxima=sums
        for i in range(k, len(nums)):
            cnt[nums[l]]-=1
            if cnt[nums[l]]==0:
                cnt.pop(nums[l])
            sums-=nums[l]
            cnt[nums[i]]+=1
            sums+=nums[i]
            
            if len(cnt)==k:
                maxima=max(maxima , sums)
            l+=1
        return maxima if maxima!=float('-inf') else 0
