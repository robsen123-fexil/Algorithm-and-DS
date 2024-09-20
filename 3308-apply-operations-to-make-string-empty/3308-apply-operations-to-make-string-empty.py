class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt=Counter(s)
        maxima=max(cnt , key=cnt.get)
        val=cnt[maxima]
        res=""
        print(val)
        cnt1=Counter()
        for i in s:
            cnt1[i]+=1
            
            if cnt1[i]==val:
                print(cnt1)
                res+=i
        return res