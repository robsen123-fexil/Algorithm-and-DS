class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt=Counter(s)
        sums=0
        odd=False
        for val in cnt.values():
            if val%2==0:
                sums+=val
            else:
                sums+=(val-1)
                odd=True
        if odd:
            sums+=1
        return sums
