class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # hsh={}
        # for i in arr:
        #     if i in hsh:
        #         hsh[i]+=1
        hsh=Counter(arr)
        print(hsh)
        res=[]
        for key , value in hsh.items():
            if value<2:
                res.append(key)
        print(res)
        if len(res)>=k:
            return res[k-1]
        else:
            return ''