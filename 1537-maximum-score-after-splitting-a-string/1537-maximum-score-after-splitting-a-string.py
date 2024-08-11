class Solution:
    def maxScore(self, s: str) -> int:
        maxscore=0
        for i in range(1 , len(s)):
            left=s[:i]
            right=s[i:]
            if left and right:

               leftcount=left.count('0')
               rightcount=right.count('1')
            sums=leftcount+rightcount
            maxscore=max(maxscore , sums)
        return maxscore