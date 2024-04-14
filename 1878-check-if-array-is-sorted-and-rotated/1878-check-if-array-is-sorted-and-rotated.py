class Solution:
    def check(self, nums: List[int]) -> bool:
        res=[]
        l=len(nums)
        for n in range(len(nums)):
            n=n%l
            res.append(nums[-n:]+nums[:-n])
        if sorted(nums) in res:
            return True
        else:
            return False

        