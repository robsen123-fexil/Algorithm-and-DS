class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res=""
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in order:
            if i in dic:
                res+=i*dic[i]
                del dic[i]
        for k , v in dic.items():
            res+=k*v
        return res


            