class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt=Counter(arr)
        res=dict(sorted(cnt.items() , key =lambda x:x[1]))
        v=[]
        for key , val in res.items():
            for i in range(val):
                v.append(key)
        cnt2=Counter(v[k:])
        return len(cnt2)
