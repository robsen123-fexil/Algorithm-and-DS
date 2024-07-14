class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=set()
        result=[]
        for i in nums:
            if i not in res:
                res.add(i)
            else:
                result.append(i)
        return result
            
