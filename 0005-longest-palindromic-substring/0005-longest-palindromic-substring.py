class Solution:
    def longestPalindrome(self, s: str) -> str:
        hsh={}
        for i in range(len(s)):
            strs=""
            for j in range(i , len(s)):
                strs+=s[j]
                if strs==strs[::-1]:
                    hsh[strs]=j-i+1
        print(hsh)
        return max(hsh , key=hsh.get)
    