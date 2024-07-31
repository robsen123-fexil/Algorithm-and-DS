class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k=0
        j=len(matrix)-1
        length=len(matrix)
        for i in matrix:
            j=len(i)-1
        while k<length and j>=0:
            if matrix[k][j]==target:
                return True
            elif matrix[k][j]>target:
                j-=1
            else:
                k+=1
        return False