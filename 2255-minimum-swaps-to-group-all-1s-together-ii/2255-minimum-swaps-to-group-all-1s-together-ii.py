class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones=nums.count(1)
        res=nums[:ones]
        print(res , ones)
        cnt=Counter(res)

        l=0
        nums=nums+nums
        minima=ones-cnt[1]
        for i in range(ones , len(nums)):
            cnt[nums[i]]+=1
            cnt[nums[l]]-=1
            if cnt[nums[l]]==0:
                cnt.pop(nums[l])
            l+=1
            minima=min(minima , ones-cnt[1])
        return minima
