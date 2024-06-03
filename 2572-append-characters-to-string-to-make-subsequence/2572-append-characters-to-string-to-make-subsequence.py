class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j=0 , 0 
        while len(s)>i and len(t)>j:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        return len(t)-j