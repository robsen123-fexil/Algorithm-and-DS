class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l=0
        # r=len(matrix)*len(matrix[0])-1
        # row=len(matrix)
        # col=len(matrix[0])
        
        # while l<=r:
        #     mid=(l+r)//2
        #     row=mid//len(matrix[0])
        #     col=mid%len(matrix[0])
        #     if matrix[row][col] < target: 
        #         l=mid+1
        #     elif matrix[row][col]>target:
        #         r=mid-1
        #     else:
        #         return True
        # return 
        t=0
        for i in range(len(matrix)):
            if matrix[i][-1]>=target:
                t=i
                break
        l=0
        r=len(matrix[t])-1
        while l<=r:
            mid=(l+r)//2
            row=mid//len(matrix)
            if matrix[t][mid]>target:
                r=mid-1
            elif matrix[t][mid]<target:
                l=mid+1
            else:
                return True
        return False
