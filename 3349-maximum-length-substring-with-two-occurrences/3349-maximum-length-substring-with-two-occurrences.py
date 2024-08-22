class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt=Counter()
        maxima=float('-inf')
        s=list(s)
        l=0
        for i in range(len(s)):
            cnt[s[i]]+=1
            while cnt[s[i]]>2:
                cnt[s[l]]-=1
                if cnt[s[l]]==0:
                    cnt.pop(s[l])
                l+=1
            maxima=max(maxima , i-l+1)
        return maxima