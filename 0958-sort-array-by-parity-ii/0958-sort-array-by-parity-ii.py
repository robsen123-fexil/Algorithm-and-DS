class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=0
        r=1
        result=[0]*len(nums)
        for i in nums:
            if i%2==0:
                result[l]=i
                l+=2
            else:
                result[r]=i
                r+=2
        return result

