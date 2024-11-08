class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        sums=maxima=l=0
        for i in range(len(s)):
            sums+=(abs(ord(s[i])-ord(t[i])))
            while sums>maxCost:
                sums-=abs(ord(s[l])-ord(t[l]))
                l+=1
            
            maxima=max(maxima , i-l+1)
        return maxima