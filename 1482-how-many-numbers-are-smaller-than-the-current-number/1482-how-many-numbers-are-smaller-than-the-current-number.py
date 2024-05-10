class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        result=[]
        num=sorted(nums)
        for i in nums:
            x=num.index(i)

            result.append(x)
        return result


        