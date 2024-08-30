class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        l=r=0
        g.sort()
        s.sort()
        while l<len(g) and l<len(s):
            if s[l]>=g[r]:
                count+=1
                r+=1

            l+=1
        return count