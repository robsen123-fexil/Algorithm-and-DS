class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minima=float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                res=nums[i]+nums[l]+nums[r]
                if abs(target-res) < abs(target-minima):
                    minima=res
                if res>target:
                    r-=1
                elif res<target:
                    l+=1
                else:
                    return res
        return minima if minima!=float('inf') else 0

