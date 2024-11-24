class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt=Counter(s)
        for i , val in enumerate(s):
            if cnt[val]==1:
                return i
        return -1