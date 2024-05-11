class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        else:
            for i in nums:
                if nums.count(i) % 2!=0:
                    return False
        return True