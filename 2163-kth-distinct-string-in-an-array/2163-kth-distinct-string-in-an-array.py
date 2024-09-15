class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt=Counter(arr)
        print(cnt)
        res=[]
        for key , value in cnt.items():
            if value ==1:
                res.append(key)
        if len(res)<k:
            return ""
        
        return res[k-1]