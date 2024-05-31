class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[]
        l=0
        maxima=0
        for i in range(len(s)):
            while s[i] in res:
                res.remove(res[l])
            res.append(s[i])
            maxima=max(len(res) , maxima)
        return maxima
            

