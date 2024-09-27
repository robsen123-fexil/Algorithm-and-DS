class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt=Counter()
        l=maxima=0
        for i in range(len(s)):
            cnt[s[i]]+=1
            while (i-l+1)-max(cnt.values())>k:
                cnt[s[l]]-=1
                l+=1
            maxima=max(maxima , i-l+1)
        return maxima


