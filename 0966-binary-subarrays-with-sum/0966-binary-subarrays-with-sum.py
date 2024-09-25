class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hsh={0:1}
        sums=count=0
        for i in range(len(nums)):
            sums+=nums[i]
            diff=(sums-goal)
            if diff in hsh:
                count+=hsh[diff]
            if sums in hsh:
                hsh[sums]+=1
            else:
                hsh[sums]=1
        return count