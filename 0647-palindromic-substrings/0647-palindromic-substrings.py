class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            strs=""
            for j in range(i , len(s)):
                strs+=s[j]
                if strs==strs[::-1]:
                    count+=1
        return count