class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        val=-1
        count=0
        for i in grid:
            for j in i:
                if j<=-1:
                    count+=1
        return count