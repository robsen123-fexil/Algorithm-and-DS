class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        s=list(s)
        val=s[:3]
        cnt=Counter(val)
        count=0
        if len(cnt)==3:
            count+=1
        l=0
        for i in range(3 , len(s)):
            val.remove(s[l])
            val.append(s[i])
            cnt=Counter(val)
            if len(cnt)==3:
                count+=1
            l+=1
        return count
       