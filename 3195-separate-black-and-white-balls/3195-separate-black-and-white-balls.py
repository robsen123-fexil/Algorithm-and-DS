class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt=0
        ones=0
        for i in s:
            if i=='1':
                ones+=1
            else:
                cnt+=ones
        return cnt