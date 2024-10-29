class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        res=[]
        for i in s:
            if i=='#' and res :
                res.pop()
            elif i!='#':
                res.append(i)
        res2=[]
        print(res)
        for i in t:
            if i=='#' and res2:
                res2.pop()
            elif i!='#':
                res2.append(i)
        print(res2)
        s1=''.join(res2)
        s2=''.join(res)
        return s1==s2

                

