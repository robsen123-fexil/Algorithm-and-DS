class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen = [-1] * 3
        ans = 0

        for i in range(len(s)):
            lastseen[ord(s[i]) - ord('a')] = i
            min_index = min(lastseen)
            ans += 1 + min_index
        
        return ans