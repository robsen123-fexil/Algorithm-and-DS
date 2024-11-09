class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res=[]
        for i in range(1 , arr[-1]+1):
            if i not in arr:
               res.append(i)
        print(res)
        if len(res)>(k-1):
            return res[k-1]
        else:
            ran=k-len(res)
            print(ran)
            for i in range(1 , ran+1):
                res.append(arr[-1]+i)
            print(res)
            return res[k-1]


        