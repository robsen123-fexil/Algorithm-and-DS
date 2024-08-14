class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        resu=[]
        for z in ranges:
            x , y=z
            for i in range(x , y+1):
               resu.append(i)
        res=[]
        for i in range(left , right+1):
            res.append(i)
        print(res , resu)
        for i in res:
            if i not in resu:
                return False
        return True
        