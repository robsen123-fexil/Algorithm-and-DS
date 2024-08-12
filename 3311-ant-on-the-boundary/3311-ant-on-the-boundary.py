class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        res=0
        for i in nums:
            res+=i
            if res==0: count+=1
        return count