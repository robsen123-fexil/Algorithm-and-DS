class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hsh={0:-1}
        sums=0
        for i , val in enumerate(nums):
            sums+=val
            rem=sums%k
            if rem not in hsh:
                hsh[rem]=i
            elif rem in hsh and (i-hsh[rem]>1):
                return True
        return False