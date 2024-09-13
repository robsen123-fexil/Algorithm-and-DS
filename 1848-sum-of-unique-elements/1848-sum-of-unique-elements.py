class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        result=0
        for key , value in cnt.items():
            if value==1:
                result+=key
        return result