class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[]
        l=0
        maxima=float('-inf')
        for i in range(len(s)):
            while s[i] in res:
                res.remove(s[l])
                l+=1
            res.append(s[i])
            maxima=max(maxima , len(res))
        return maxima if maxima!= float('-inf') else 0
