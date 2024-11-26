class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt=Counter(s)
        cnt2=Counter(t)
        count=0
        for key , val in cnt2.items():
            if key in cnt:
                if cnt[key]<val:

                    count+=abs(val-cnt[key])
            else:
                count+=val
        return count