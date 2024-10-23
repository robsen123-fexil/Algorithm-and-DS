class Solution:
    def minimumSteps(self, s: str) -> int:
        s=list(s)
        ones=ans=r=0
        while r<len(s):
            if s[r]=='1':
                ones+=1
            else:
                ans+=ones
            r+=1
        return ans
