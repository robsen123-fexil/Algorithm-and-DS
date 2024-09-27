class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l=0
        maxima=0
        for i in range(len(nums)):
            res=[]
            if nums[i]%2==0 and nums[i]<=threshold:
                res.append(0)   
            else:
                continue
            for j in range(i+1 , len(nums)):
                if res[-1]!=nums[j]%2 and nums[j]<=threshold:
                    res.append(nums[j]%2)
                else:
                    break
            maxima=max(maxima , len(res))
        return maxima
            