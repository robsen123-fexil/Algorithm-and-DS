class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        l=r=0
        while l<len(matrix[0]):
            result.append([])
            
            for i in range(len(matrix)):
                result[-1].append(matrix[i][l])
            l+=1
        return result
