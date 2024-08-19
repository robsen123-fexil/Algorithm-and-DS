class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=0
        curcost=0
        maxima=float('-inf')
        for x , ( i , j)  in enumerate(zip(s , t)):
            curcost+=abs(ord(j)-ord(i))
            while curcost>maxCost:
                curcost-=abs(ord(s[l])-ord(t[l]))
                l+=1
                maxima=max(maxima , x-l+1)
            maxima=max(maxima ,x-l+1)
        return maxima
            
