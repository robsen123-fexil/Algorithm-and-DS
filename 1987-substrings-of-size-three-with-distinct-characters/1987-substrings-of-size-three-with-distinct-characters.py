class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res=list(s[:3])
        cnt=Counter(res)
        count=0
        if len(cnt)==3:
            count+=1
        l=0
        for i in range(3 , len(s)):
            res.append(s[i])
            res.remove(s[l])
            l+=1
            cnt=Counter(res)
            if len(cnt)==3:
                count+=1
        return count
        