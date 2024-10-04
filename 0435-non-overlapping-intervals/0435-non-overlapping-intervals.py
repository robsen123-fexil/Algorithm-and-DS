class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result=[]
        intervals.sort()
        count=0
        result.append(intervals[0])
        print(intervals)
        for i in range(1 , len(intervals)):
            x , y =result[-1]
            a , b = intervals[i]
            if y>a:
                count+=1
                mini=min(x ,a)
                minii=min(y , b)
                result.append([mini  , minii])
            else:
                result.append(intervals[i])
        print(result)
        return count