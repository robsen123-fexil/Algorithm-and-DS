class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            res.append(i)
        for i in nums:
            res.append(int(str(i)[::-1]))
        cnt=set(res)
        return len(cnt)
        