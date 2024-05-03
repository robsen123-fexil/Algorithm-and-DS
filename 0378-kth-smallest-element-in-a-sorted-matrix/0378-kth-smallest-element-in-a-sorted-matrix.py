class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        res=[]
        for i in matrix:
            for j in i:
                res.append(j)

        res.sort()
        return res[k-1]
        
