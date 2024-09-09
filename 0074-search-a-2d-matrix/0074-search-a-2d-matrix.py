class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l=0
            r=len(i)-1
            if i[l]<=target<=i[r]:
                while l<=r:
                    if target==i[r]:
                        return True
                    r-=1
        return False