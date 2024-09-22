class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[intervals[0]]
        intervals=sorted(intervals , key=lambda x:x[0])
        res=[intervals[0]]
        print
        for i in range(1 , len(intervals)):
            a , b= res[-1]
            x , y = intervals[i]
            if b<x:
                print("g")
                res.append(intervals[i])
            else:
                print("heh")
                
                res[-1][0]=min(res[-1][0] , x)
                res[-1][1]= max(res[-1][1] , y)
        return res