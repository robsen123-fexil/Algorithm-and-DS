class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=first=0
        sums=sum(nums)
        for i in range(len(nums)):
            if i!=len(nums)-1:
              first+=nums[i]
              sums-=nums[i]
              print(sums , first)
              if first>=sums:count+=1
            
        return count