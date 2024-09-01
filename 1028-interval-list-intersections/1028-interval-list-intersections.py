
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l=r=0
        result=[]
        while l < len(firstList) and r<len(secondList):
            i , j  = firstList[l]
            x , y = secondList[r]
            maxima=max(i , x)
            minima=min(j , y)
            if minima>=maxima:
                result.append([maxima , minima])
            if j<y:
                l+=1
            else:
                r+=1
        return result
            
            