class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        cnt=Counter(s)
        for i in cnt:
            if cnt[i]==1:
                return s.index(i)
        return -1
