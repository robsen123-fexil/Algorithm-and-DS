class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res=[]
        l=0
        maxima=float('-inf')
        cnt=Counter()
        for i in range(len(word)):
            
            if not res:
                res.append(word[i])
                cnt[word[i]]+=1
            else:
                s=ord(res[-1])
                if s>ord(word[i]):
                    l=i
                    res=[]
                    res.append(word[l])
                    cnt=Counter()
                    cnt[word[l]]+=1
                else:
                    res.append(word[i])
                    cnt[word[i]]+=1
            if len(cnt)==5:
                maxima=max(maxima , i-l+1)
        return maxima if maxima!=float('-inf') else 0
            