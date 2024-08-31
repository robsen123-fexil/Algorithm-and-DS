class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        hsh=defaultdict(list)
        for i , val  in enumerate(s):
            if val == c:
                hsh[c].append(i)
        res=sorted(hsh[c])
        s=list(s)
        l=0
        result=[]
        print(res)
        for i , val in enumerate(s):
            mini=float('inf')
            for j in res:
                ll=abs(j-i)
                if mini>=ll:
                    mini=ll
            result.append(mini)

        return result