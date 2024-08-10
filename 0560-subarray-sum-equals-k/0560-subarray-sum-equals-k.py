class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hsh={0:1}
        sums=count=0
        for i  , val in enumerate(nums):
            sums+=val
            diff=sums-k
            if diff in hsh:
                count+=hsh[diff]
            hsh[sums]=hsh.get(sums , 0)+1
        return count
