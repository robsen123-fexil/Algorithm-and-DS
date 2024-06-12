class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        res.append([])
        for i in nums:
            for j in range(len(res)):
                sub=res[j].copy()
                sub.append(i)
                if not sorted(sub) in res:

                   res.append(sorted(sub))
        return res
        