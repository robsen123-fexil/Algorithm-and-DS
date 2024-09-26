class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        res=nums[:k]
        maxima=max(res)-min(res)
        l=0
        print(res)
        for i in range(k, len(nums)):
            
            res.append(nums[i])
            res.remove(nums[l])
            l+=1
            
            maxima=min(maxima , (max(res)-min(res)))
        return maxima