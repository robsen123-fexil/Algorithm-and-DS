class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result=[]
        intervals=sorted(intervals , key =lambda x:(x[0]  , -x[1] ))
        result.append(intervals[0])
        for i in range(1 , len(intervals)):
            x , y = result[-1]
            a , b = intervals[i]
            if x<=a and y>=b:
                continue
            else:
                result.append(intervals[i])
        return len(result) 