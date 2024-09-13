class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt=Counter(s)
        cnt2=Counter(t)
        count=0
        for key , value in cnt2.items():
            val=cnt[key]
            if value>val:
                count+=abs(value-val)
        return count
        