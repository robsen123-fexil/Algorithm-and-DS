class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1=Counter(s)
        cnt2=Counter(t)
        count=0
        for key , value in cnt1.items():
            val=cnt2[key]
            if value > val :
                count+=(value-val)
        for key , value in cnt2.items():
            val=cnt1[key]
            if value>val:
                count+=(value-val)
                
        return count