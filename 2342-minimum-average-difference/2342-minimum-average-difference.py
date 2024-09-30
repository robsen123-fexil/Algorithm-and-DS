from typing import List
from math import inf

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        mini = inf
        ind = -1
        left = 0
        sums = sum(nums)
        
        for i in range(len(nums)):
            sums -= nums[i]
            left += nums[i]
            l = left // (i + 1)

            if i == len(nums) - 1:
                r = 0  
            else:
                r = sums // (len(nums) - (i + 1))

            avg = abs(l - r)
           
            if avg < mini:
                mini = avg
                ind = i
                
        return ind
