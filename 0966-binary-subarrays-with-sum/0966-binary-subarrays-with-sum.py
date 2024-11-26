class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hsh={0:1}
        sums=count=0
        for i in range(len(nums)):
            sums+=nums[i]
            if sums-goal in hsh:
                count+=hsh[sums-goal]
                
            if sums not in hsh:
                hsh[sums]=1
            else:
                hsh[sums]+=1
        return count