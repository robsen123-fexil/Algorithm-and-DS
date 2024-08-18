class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(list(s1))
        s2=list(s2)

        for i in range(len(s2)-len(s1)+1):
            res=sorted(s2[i:i+len(s1)])
            if res==s1:
                return True
        return False