class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l=count=0
        r=len(nums)-1
        nums.sort()
        while l<r:
            res=nums[l]+nums[r]
            if res>k:
                r-=1
            elif res<k:
                l+=1
            else:
                print(nums[r] , nums[l])
                count+=1
                l+=1
                r-=1
        return count