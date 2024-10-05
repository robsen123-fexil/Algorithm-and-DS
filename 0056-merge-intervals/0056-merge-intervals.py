class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        result.append(intervals[0])
        for i in range(1 , len(intervals)):
            x , y = result[-1]
            a , b =intervals[i]
            if y>=a:
                maxima=max(y , b)
                result[-1][1]=maxima
            else:
                result.append([a , b])
        return result