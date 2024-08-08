class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums=0
        hsh={0:1}
        count=0
        for i in nums:
            sums+=i
            diff=sums-k
            if diff in hsh:
                count+=hsh[diff]
            hsh[sums]=hsh.get(sums , 0)+1
        return count
