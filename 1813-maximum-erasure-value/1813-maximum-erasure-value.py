class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxima=float('-inf')
        cnt=Counter()
        sums=l=0
        for i in range(len(nums)):
            while nums[i] in cnt:
                cnt[nums[l]]-=1
                sums-=nums[l]
                if cnt[nums[l]]==0:
                    cnt.pop(nums[l])
                l+=1
            cnt[nums[i]]+=1
            sums+=nums[i]
            maxima=max(maxima  , sums)
        return  maxima