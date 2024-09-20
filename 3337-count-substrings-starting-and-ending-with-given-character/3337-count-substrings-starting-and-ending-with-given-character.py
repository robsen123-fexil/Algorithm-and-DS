class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        ans=0
        cnt=Counter()
        for i in s:
            cnt[i]+=1
            if c==i:
                ans+=cnt[i]
        return ans