class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxima=defaultdict(list)
        l=r=0
        s=list(s)
        for i in range(len(s)):
            strs=""
            for j in range(i, len(s)):
                strs+=s[j]
                if strs==strs[::-1]:
                    maxima[j-i+1]=strs
        return maxima[max(maxima)]
                


