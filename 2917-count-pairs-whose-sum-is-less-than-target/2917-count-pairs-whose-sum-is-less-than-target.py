class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res=[]
        n=len(nums)
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                if i < j < n and (nums[i]+nums[j])<target:
                    res.append([i , j])
        return len(res)
        