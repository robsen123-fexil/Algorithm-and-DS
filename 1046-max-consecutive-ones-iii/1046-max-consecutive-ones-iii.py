class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=l=r=maxima=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            if count>k:
                while nums[l]!=0:
                    l+=1
                count-=1
                l+=1
            maxima=max(maxima , i-l+1)
        return maxima