class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        l=0
        r=len(nums)-1
        nums.sort()
        res=[]
        while l<r:
            sums=(nums[l]+nums[r])/2
            res.append(sums)
            l+=1
            r-=1
        return min(res)
            
