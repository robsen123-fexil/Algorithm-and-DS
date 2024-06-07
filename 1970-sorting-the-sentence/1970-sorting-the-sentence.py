class Solution:
    def sortSentence(self, s: str) -> str:
        
        ss=s.split()
        l=len(ss)+1
        res1=[0]*l
        res2=[]
        for i in range(len(ss)):
            for j in ss[i]:
                if j.isdigit():
                    res1[int(j)]=ss[i]
                    break
        result=res1[1:]
        for i in result:
            st=""
            for j in i:
                if not j.isdigit():
                    st+=j
            res2.append(st)
        return " ".join(res2)
                
        
        