class Solution:
    def maxScore(self, s: str) -> int:
        maxima=0
        
        for i in range(1 , len(s)):
            left=s[:i]
            right=s[i:]
            lef=Counter(left)

            righ=Counter(right)
            maxima=max(maxima  , lef['0']+righ['1'])
        return maxima