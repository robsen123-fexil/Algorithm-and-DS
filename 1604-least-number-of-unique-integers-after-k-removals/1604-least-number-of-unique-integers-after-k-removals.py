class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt=Counter(arr)
        res=dict(sorted(cnt.items() , key= lambda x:x[1]))
        result=[]
        for key , value in res.items():
            for i in range(value):
                result.append(key)
        print(result)
        resu=set()
        for i in range(k , len(result)):
            
            resu.add(result[i])
        return len(resu)
