class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        s=list(s)
        p=list(sorted(p))
        for i in range(len(s)-len(p)+1):
            res=sorted(s[i:i+len(p)])
            if p==res:
                result.append(i)
        return result

