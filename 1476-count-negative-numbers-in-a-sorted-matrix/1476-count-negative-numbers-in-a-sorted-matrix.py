class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt=0
        for i in grid:
            l=0
            r=len(i)-1
            while l<=r:
                if i[r]<0:
                    cnt+=1
                r-=1
        return cnt
