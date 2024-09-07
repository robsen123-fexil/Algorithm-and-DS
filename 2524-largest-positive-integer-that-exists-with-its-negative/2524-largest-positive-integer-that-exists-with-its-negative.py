class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxima=float('-inf')
        for i in nums:
            val=i
            if not i<0 and val*-1 in nums:
                maxima=max(maxima , i )
        return maxima if maxima!=float('-inf') else -1