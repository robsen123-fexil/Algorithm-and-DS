class Solution:
    def beautySum(self, s: str) -> int:
        cnt=Counter()
        result=0
        for i in range(len(s)):
            res=s[i]
            for j in range(i+1 , len(s)):
                
                res+=s[j]
                cnt=Counter(res)
                maxima=max(cnt  , key=cnt.get)
                minima=min(cnt , key=cnt.get)
                if minima!=maxima:
                   result+=(cnt[maxima]-cnt[minima])
        return result
                