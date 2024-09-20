class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt=Counter(nums)
        
        for val in cnt.values():
            if val>2:
                return False
        return True

        