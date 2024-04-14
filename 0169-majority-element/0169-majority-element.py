class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        cand=0
        n=len(nums)
        for num in nums:
            if count==0:
                cand=num
            if num==cand:
                count+=1
            else:
                count-=1     
        return cand   