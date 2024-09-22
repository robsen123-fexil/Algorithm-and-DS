class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals  , key = lambda x:x[0])
        res=[intervals[0]]
        for i in range(1 , len(intervals)):
            x , y= res[-1]
            a  , b = intervals[i]
            if a>y:
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1] ,  b)
        return res
