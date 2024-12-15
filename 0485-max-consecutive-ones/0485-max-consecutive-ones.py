class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        strs=""
        for i in nums:
            strs+=str(i)
        

        val=strs.split('0')
        res=[]
        for i in val:
            res.append(len(i))
        return max(res)