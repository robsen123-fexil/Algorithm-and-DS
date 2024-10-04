class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result=[]
        result.append(intervals[0])
        for i in range(1 , len(intervals)):
            x , y = result[-1]
            a , b = intervals[i]
            if y>=a:
                result[-1][1]=max(y , b)
            else:
                result.append(intervals[i])
        return result