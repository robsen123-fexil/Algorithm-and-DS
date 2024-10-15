class Solution:
    def minimumSteps(self, s: str) -> int:
        count=one=0
        for i in s:
            if i=='1':
                one+=1
            else:
                count+=one
        return count
