class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=set()
        for i in nums:
            num.add(i)
        res=[i for i in num]
        res.sort()
        resu=res[::-1]
        if len(resu)>=3:
            return resu[3-1]
        else:
            return max(resu) 