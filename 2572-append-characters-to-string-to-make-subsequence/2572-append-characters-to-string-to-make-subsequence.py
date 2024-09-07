class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l=r=cnt=0
        s=list(s)
        if t[0] in s:

           s=s[s.index(t[0]):]
        else:
            return len(t)
            
        while l<len(s) and r<len(t):
            if s[l]==t[r]:
                l+=1
            else:
                cnt+=1
            r+=1
        return cnt
