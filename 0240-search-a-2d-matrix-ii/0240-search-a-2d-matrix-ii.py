class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])-1 , -1 , -1):
                if target<matrix[i][j]:
                    j-=1
                elif target>matrix[i][j]:
                    break
                else:
                    return True
        return False