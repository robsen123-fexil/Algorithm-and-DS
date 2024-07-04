class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        res=[]
        for i  , j in zip(pos , neg):
            res.append(i)
            res.append(j)
        return res