class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=r=count=0
        for i in s:
            if i=='R':
                r+=1
            elif i=='L':
                l+=1
            if r==l:
                count+=1
        return count