class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result=[]
        for i in range(len(nums)):
            r=i+1
            result.append(nums[i])
            res=nums[i]
            while r<len(nums):
                res+=nums[r]
                result.append(res)
                r+=1
        result.sort()
        left-=1
        Mod=10**9+7
        sums=sum(result[left:right])%Mod
        print
        return sums
