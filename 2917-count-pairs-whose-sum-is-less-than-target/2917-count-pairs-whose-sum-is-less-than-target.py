class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=count=0
        r=len(nums)-1
        while l<r:
            res=nums[l]+nums[r]
            if res>=target:
                r-=1
            else:
                
                count+= (r-l)
                l+=1
        return count 
        