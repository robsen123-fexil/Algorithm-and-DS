class Solution(object):
    def findMiddleIndex(self, nums):
        rightSum,leftSum = sum(nums),0
        for i,num in enumerate(nums):
            if leftSum == rightSum-num:
                return i
            leftSum += num
            rightSum -= num
        return -1