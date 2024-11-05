class Solution:
    def minChanges(self, s: str) -> int:

        count=0
        r=0
        while r<len(s)-1:
            if s[r]!=s[r+1]:
                count+=1
            r+=2
        return count
