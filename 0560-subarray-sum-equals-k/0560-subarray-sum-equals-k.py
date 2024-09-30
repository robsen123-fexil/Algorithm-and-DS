class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums=l=count=0
        hsh={0:1}
        for i in range(len(nums)):
            sums+=nums[i]
            if sums-k in hsh:
                count+=hsh[sums-k]
            if sums not in hsh:
                hsh[sums]=1
            else:
                hsh[sums]+=1
        return count