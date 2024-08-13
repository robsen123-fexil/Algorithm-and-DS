class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sums=sum(nums)
        summs=0
        result=[]
        for i in nums:
            summs+=i
            result.append(abs(sums-summs-(summs-i)))
        return result

    