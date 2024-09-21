class Solution:
    def minimumLength(self, s: str) -> int:
        cnt=Counter(s)
        count=0
        for val in cnt.values():
            if val<=2:
                count+=val
            else:
                while val>=3:
                    val-=2
                count+=val
        return count

        