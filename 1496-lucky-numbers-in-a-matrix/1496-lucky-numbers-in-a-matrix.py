class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result=[]
        for i in range(len(matrix)):
            minima=min(matrix[i])
            indexs=matrix[i].index(minima)
            res=[]
            for i in range(len(matrix)):
                res.append(matrix[i][indexs])
            maxima=max(res)
            if maxima==minima:
                result.append(minima)
        return result        