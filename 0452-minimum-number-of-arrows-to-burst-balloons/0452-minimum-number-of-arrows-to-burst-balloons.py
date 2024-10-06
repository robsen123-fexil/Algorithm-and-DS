class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        nums=sorted(points , key=lambda x:x[1])
        count=0
        large=-inf
        for i in range(len(nums)):
            a , b = nums[i]
            if a>large:
                count+=1
                large=b
        return count


    