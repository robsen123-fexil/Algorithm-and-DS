class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt=Counter(s)
        maxima=max(cnt , key=cnt.get)
        val=cnt[maxima]
        for key , value in cnt.items():
            if val!=value:
                return False
        return True