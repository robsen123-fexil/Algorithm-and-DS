class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res=[]
        for i in nums:
            for j in i:
                res.append(j)
        cnt=Counter(res)
        result=[]
        for key , val in cnt.items():
            if val==len(nums):
                result.append(key)
        sorte=sorted(result)
        return sorte