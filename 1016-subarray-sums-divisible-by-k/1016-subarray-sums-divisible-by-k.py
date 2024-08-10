class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hsh={0:1}
        count=sums=0
        for i in  range(len(nums)):
            sums+=nums[i]
            res=sums%k
            if res in hsh:
                count+=hsh[res]
                hsh[res]+=1
            else:
                hsh[res]=1
        return count

                
            