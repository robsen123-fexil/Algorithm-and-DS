class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res=list(s[:k])
        cnt=Counter(res)
        vowels='aeiou'
        count=0
        for i in vowels:
            if i in cnt:
                count+=cnt[i]
        maxima=count
        l=0
        for i in range(k , len(s)):
            cnt[s[l]]-=1
            cnt[s[i]]+=1
            l+=1
            count=0
            for j in vowels:
                if j in cnt:
                    count+=cnt[j]
            maxima=max(maxima , count)
        return maxima
